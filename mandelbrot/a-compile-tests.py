import os
import re
import csv

# Define the filename pattern
filename_pattern = re.compile(r'^perf-mandelbrot-(\d+)-(\w)-(\d+)-(\d+)\.txt$')

def decompose_filename(filename):
    match = filename_pattern.match(filename)
    if match:
        thread_count = int(match.group(1))
        schedule_type = match.group(2)
        chunk_size = int(match.group(3))
        iteration = int(match.group(4))
        return thread_count, schedule_type, chunk_size, iteration
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
        csv_writer.writerow(['File', 'Thread Count', 'Schedule Type', 'Chunk Size', 'Iteration', 'Mixed Test Time', 'White Test Time', 'Black Test Time'])

        # Iterate through files in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Check if it's a file and matches the expected pattern
            if os.path.isfile(file_path) and filename_pattern.match(filename):
                # Decompose filename
                thread_count, schedule_type, chunk_size, iteration = decompose_filename(filename)
                if "s" in schedule_type:
                    schedule_type = "static"
                elif "d" in schedule_type:
                    schedule_type = "dynamic"
                # Extract test times
                test_times = extract_test_times(file_path)

                # Write the information to the CSV file
                csv_writer.writerow([filename, thread_count, schedule_type, chunk_size, iteration,
                                     test_times['zoom_in_test_mixed'],
                                     test_times['zoom_in_test_all_white'],
                                     test_times['zoom_in_test_all_black']])

# Example usage
directory_path = "./perf-test-a"
output_csv_path = "a-tests.csv"

process_directory(directory_path, output_csv_path)
