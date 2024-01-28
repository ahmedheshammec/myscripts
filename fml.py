#!/usr/bin/env python3

import sys
import re

def fix_mixed_language_line(line):
    words = line.split()
    if re.search(r'[a-zA-Z]', words[-1]): 
        words = [words[-1]] + words[:-1]
        line = ' '.join(words)
    return line

def process_srt_file(file_path):
    output_lines = []
    
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        for line in f:
            if line.strip(): 
                line = fix_mixed_language_line(line)
            output_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python fml.py <file>") 
        sys.exit()
    
    srt_file = sys.argv[1]  
    process_srt_file(srt_file)
    
    print("SRT file processed successfully!")