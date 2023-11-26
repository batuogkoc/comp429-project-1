import os
from os import path
import re

def extract_elapsed_time(text):
    # Define the regular expression pattern to match the "Elapsed time" line
    pattern = r'Elapsed time: (\d+\.\d+)'

    # Use re.search to find the match in the text
    match = re.search(pattern, text)

    # Check if a match is found
    if match:
        # Extract and return the elapsed time value
        elapsed_time = float(match.group(1))
        return elapsed_time
    else:
        # Return None if no match is found
        return None

if __name__ == "__main__":
    DIR="./perf-test-a"
    ret = {}
    for file in os.listdir(DIR):
        pattern = r'perf-()- time: (\d+\.\d+)'
        if file[0:4] == "perf":
            print(file, end=" ")
            with open(os.path.join(DIR, file), "r") as f:
                time = extract_elapsed_time(f.read())
                if time is None:
                    print("ERROR")
                else:
                    print(time)