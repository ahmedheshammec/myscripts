#!/usr/bin/env python3

# This Script Fixes the Rendering of the Following Characters [!] [.] [،] in the Srt Files

import sys
import re

import_choice = None

def move_punctuation(line):
    line = line.strip()  # Remove leading and trailing whitespace
    line = line.replace('"', '')  # Remove "
    line = line.replace("'", '')  # Remove '
    punctuation = ['!', '،', ':', '...', '.', '-']  # Add more characters here if needed
    for p in punctuation:
        if line.endswith(p):
            line = p + line[:-1]
            break
    return line

def process_srt_file(file_path):

    global timecode_adjust
    
    while import_choice not in ['a', 'd']:
        import_choice = input("Enter 'a' to advance timecodes, 'd' to delay: ")
        
    if import_choice == 'a':
        timecode_adjust = 0.5  # Advance
    else:
        timecode_adjust = -0.5 # Delay
        
    output_lines = []
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        for line in file:
            if re.match(r'^\d{1,}$', line):
                output_lines.append(line)  # Preserve subtitle number
            elif re.match(r'^\d{1,2}:\d{2}:\d{2},\d{3} --> \d{1,2}:\d{2}:\d{2},\d{3}$', line):
                output_lines.append(line)  # Preserve timestamps
            elif line.strip():  # Move punctuation in non-empty lines
                output_line = move_punctuation(line)
                output_lines.append(output_line + '\n')
            else:
                output_lines.append(line)  # Preserve empty lines
    
    # Write modified lines back to the original file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(output_lines)

if __name__ == '__main__':
    srt_file_path = sys.argv[1]  
    process_srt_file(srt_file_path)
    if len(sys.argv) != 2:
        print("Usage: python move_punctuation.py <file-path>")
    else:
        srt_file_path = sys.argv[1]
        process_srt_file(srt_file_path)
        print("SRT file processed successfully!")
