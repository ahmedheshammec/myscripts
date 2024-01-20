#!/usr/bin/env python3

import sys
import pyarabic.araby as araby
import pyarabic.number as number
from pyarabic.araby import strip_tatweel

# Check if the file path argument is provided
if len(sys.argv) != 2:
    print("Please provide the file path as an argument.")
    sys.exit(1)

file_path = sys.argv[1]

# Open the file for reading
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Apply the strip_tatweel function to each line
modified_lines = [strip_tatweel(line) for line in lines]

# Open the file for writing
with open(file_path, "w", encoding="utf-8") as file:
    # Write the modified lines back to the file
    file.writelines(modified_lines)
