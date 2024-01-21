#!/usr/bin/env python3

# This Script Makes Adjustment to the Given Srt file Given it's Path as Argument when you run the Script

import sys
import shutil
import os

def delay_srt_timing(input_file, action, seconds):
    temp_file = input_file + '.temp'

    with open(input_file, 'r') as infile, open(temp_file, 'w') as outfile:
        for line in infile:
            if '-->' in line:
                start_time, end_time = line.strip().split(' --> ')
                start_time_parts = start_time.split(':')
                end_time_parts = end_time.split(':')

                start_seconds = int(start_time_parts[0]) * 3600 + int(start_time_parts[1]) * 60 + float(start_time_parts[2].replace(',', '.'))
                end_seconds = int(end_time_parts[0]) * 3600 + int(end_time_parts[1]) * 60 + float(end_time_parts[2].replace(',', '.'))

                if action == 'a':
                    new_start_seconds = start_seconds + seconds  # Advance timing
                    new_end_seconds = end_seconds + seconds
                else:
                    new_start_seconds = start_seconds - seconds  # Delay timing
                    new_end_seconds = end_seconds - seconds

                new_start_time = '{:02}:{:02}:{:06.03f}'.format(
                    int(new_start_seconds // 3600),
                    int((new_start_seconds % 3600) // 60),
                    new_start_seconds % 60
                )

                new_end_time = '{:02}:{:02}:{:06.03f}'.format(
                    int(new_end_seconds // 3600),
                    int((new_end_seconds % 3600) // 60),
                    new_end_seconds % 60
                )

                adjusted_line = "{0} --> {1}\n".format(new_start_time.replace('.', ','), new_end_time.replace('.', ','))
                outfile.write(adjusted_line)
            else:
                outfile.write(line)

    # Move the temporary file to the original input file
    shutil.move(temp_file, input_file)

    print("All Done! Timing {}ed by {} seconds for file '{}'".format("Advance" if action == 'a' else "Delay", seconds, input_file))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Srt [Advance & Delay].py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    action = input("Choose either Delay or Advance (d/a): ").lower()
    seconds = int(input("Enter the number of seconds: "))

    if action not in ('d', 'a'):
        print("Invalid action.")
        sys.exit(1)

    delay_srt_timing(input_file, action, seconds)
