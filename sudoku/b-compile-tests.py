import os
import re
import csv

# Define the filename pattern
filename_pattern = re.compile(r'^perf-(\w+)-(\w+)-(\d+)-(\d+)\.txt$')

def decompose_filename(filename):
    match = filename_pattern.match(filename)
    if match:
        exec_value = match.group(1)
        test_file = match.group(2)
        thread_count = int(match.group(3))
        iteration = int(match.group(4))
        return exec_value, test_file, thread_count, iteration
    else:
        return None

def extract_elapsed_time(file_path):
    with open(file_path, 'r') as file:
        # Read the file and look for the "Elapsed time" line
        for line in file:
            if line.startswith('Elapsed time:'):
                # Extract and return the elapsed time value
                return float(line.split(':')[1].strip())

    # Return None if the "Elapsed time" line is not found
    return None

def process_directory(directory_path, output_csv_path):
    # Create a CSV file for output
    with open(output_csv_path, 'w', newline='') as csv_file:
        # Define CSV writer
        csv_writer = csv.writer(csv_file)

        # Write header to the CSV file
        csv_writer.writerow(['File', 'Exec Value', 'Test File', 'Thread Count', 'Iteration', 'Elapsed Time'])

        # Iterate through files in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            # Check if it's a file and matches the expected pattern
            if os.path.isfile(file_path) and filename_pattern.match(filename):
                # Decompose filename
                exec_value, test_file, thread_count, iteration = decompose_filename(filename)

                # Extract elapsed time
                elapsed_time = extract_elapsed_time(file_path)

                # Write the information to the CSV file
                csv_writer.writerow([filename, exec_value, test_file, thread_count, iteration, elapsed_time])

# Example usage
directory_path = "./perf-test-b"
output_csv_path = "b-perf-test.csv"

process_directory(directory_path, output_csv_path)
