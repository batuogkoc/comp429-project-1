import os
from os import path

DIR="./perf-test"
ret = {}
for file in os.listdir(DIR):
    if file[0:4] == "perf":
        print(file, end=" ")
        with open(os.path.join(DIR, file), "r") as f:
            print(f.readlines()[-1])