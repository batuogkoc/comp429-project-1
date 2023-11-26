import os
import re
import csv

# Define the filename pattern
filename_pattern = re.compile(r'^perf-(\w+)-(\d+)-(\d+)\.txt$')

def decompose_filename(filename):
    match = filename_pattern.match(filename)
    if match:
        exec_value = match.group(1)
        thread_count = int(match.group(2))
        iteration = int(match.group(3))
        return exec_value, thread_count, iteration
    else:
        return None

def extract_test_times(file_path):
    test_times = {'zoom_in_test_mixed': None, 'zoom_in_test_all_white': None, 'zoom_in_test_all_black': None}

    with open(file_path, 'r') as file:
        for line in file:
            # Check for lines containing the specified patterns
            if "Finished test ( zoom_in_test_mixed) in:" in line:
                test_times['zoom_in_test_mixed'] = int(line.split(":")[1].strip().split()[0])
            elif "Finished test ( zoom_in_test_all_white) in:" in line:
                test_times['zoom_in_test_all_white'] = int(line.split(":")[1].strip().split()[0])
            elif "Finished test ( zoom_in_test_all_black) in:" in line:
                test_times['zoom_in_test_all_black'] = int(line.split(":")[1].strip().split()[0])

    return test_times

def process_directory(directory_path, output_csv_path):
    # Create a CSV file for output
    with open(output_csv_path, 'w', newline='') as csv_file:
        # Define CSV writer
        csv_writer = csv.writer(csv_file)

        # Write header to the CSV file
        csv_writer.writerow(['File', 'Exec Value', 'Thread Count', 'Iteration', 'Mixed Test Time', 'White Test Time', 'Black Test Time'])

        # Iterate through files in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Check if it's a file and matches the expected pattern
            if os.path.isfile(file_path) and filename_pattern.match(filename):
                # Decompose filename
                exec_value, thread_count, iteration = decompose_filename(filename)

                # Extract test times
                test_times = extract_test_times(file_path)

                # Write the information to the CSV file
                csv_writer.writerow([filename, exec_value, thread_count, iteration,
                                     test_times['zoom_in_test_mixed'],
                                     test_times['zoom_in_test_all_white'],
                                     test_times['zoom_in_test_all_black']])

# Example usage
directory_path = "./perf-test-a"
output_csv_path = "a-tests.csv"

process_directory(directory_path, output_csv_path)
