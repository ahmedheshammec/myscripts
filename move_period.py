#!/usr/bin/env python3

# This Script Fixes the Rendering of the Following Characters [!] [.] [،] in the Srt Files

# Also has Function for Mixed English Arabic Words in the Same line. 

import sys
import re

def fix_mixed_language_line(line):
    words = line.split()
    if re.search(r'[a-zA-Z]', words[-1]):
        words = [words[-1]] + words[:-1] 
        line = ' '.join(words)
    return line

def move_punctuation(line):
    line = line.strip() 

    line = fix_mixed_language_line(line)

    line = line.replace('"', '')  
    line = line.replace("'", '')   
    line = line.replace("- ", '')   
    line = line.replace("<i>", '')   
    line = line.replace("</i>", '')   
    line = line.replace("(", '')   
    line = line.replace(")", '')   
    line = line.replace(".", '')   
    line = line.replace("  ", ' ')   
    line = re.sub(r"^((?!\d{2}:\d{2}:\d{2},\d{3}).)*$", lambda x: x.group(0).replace("-", ""), line)
    line = re.sub(r"^((?!\d{2}:\d{2}:\d{2},\d{3}).)*$", lambda x: x.group(0).replace("--", ""), line)

    punctuation = ['!', '،', ':', '...', '.', '-']

    for p in punctuation:
        if line.endswith(p):
            line = p + line[:-1]
            break

    return line

def process_srt_file(file_path):

    output_lines = []
    
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        for line in file:
            if re.match(r'^\d+$', line): 
                output_lines.append(line)

            elif re.match(r'^\d{1,2}:\d{2}:\d{2},\d{3} --> \d{1,2}:\d{2}:\d{2},\d{3}$', line):
                output_lines.append(line)   

            elif line.strip():
                line = move_punctuation(line)
                output_lines.append(line + '\n')

            else:
                output_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(output_lines)
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python move_punctuation.py <file-path>")
    else:
        srt_file_path = sys.argv[1]
        process_srt_file(srt_file_path)
        print("SRT file processed successfully!")