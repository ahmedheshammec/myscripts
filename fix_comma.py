#!/usr/bin/env python3

import sys

def update_srt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if ' --> ' in line:
                line = line.replace('،', ',')
            file.write(line)

if len(sys.argv) > 1:
    srt_file_path = sys.argv[1]
    update_srt_file(srt_file_path)
else:
    print("Please provide the SRT file path as an argument.")
