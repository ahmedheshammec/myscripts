#!/usr/bin/env python3
import sys
import shutil

def adjust_srt_timing(input_file, action, time_adjustment):
    temp_file = input_file + '.temp'

    with open(input_file, 'r') as infile, open(temp_file, 'w') as outfile:
        for line in infile:
            if '-->' in line:
                start_time, end_time = line.strip().split(' --> ')
                new_start_time = adjust_time(start_time, action, time_adjustment)
                new_end_time = adjust_time(end_time, action, time_adjustment)
                adjusted_line = "{} --> {}\n".format(new_start_time, new_end_time)
                outfile.write(adjusted_line)
            else:
                outfile.write(line)

    shutil.move(temp_file, input_file)
    print("All Done! Timing {}ed by {} for file '{}'".format("advanced" if action == 'a' else "delayed", time_adjustment, input_file))

def adjust_time(time_str, action, time_adjustment):
    hours, minutes, rest = time_str.split(':')
    seconds, milliseconds = rest.split(',')
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds) + float('0.' + milliseconds)

    if action == 'a':
        total_seconds += time_adjustment
    else:
        total_seconds -= time_adjustment

    new_hours = int(total_seconds // 3600)
    new_minutes = int((total_seconds % 3600) // 60)
    new_seconds = int(total_seconds % 60)
    new_milliseconds = int((total_seconds % 1) * 1000)

    return "{:02}:{:02}:{:02},{:03}".format(new_hours, new_minutes, new_seconds, new_milliseconds)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Srt [Advance & Delay].py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Improved error handling for action input
    while True:
        action = input("Choose either Delay or Advance (d/a): ").lower()
        if action in ('d', 'a'):
            break
        else:
            print("Invalid action. Please enter 'd' for delay or 'a' for advance.")

    # Handling the time input
    while True:
        time_input = input("Enter the number of seconds (integer or float): ")
        try:
            time_adjustment = float(time_input)
            break
        except ValueError:
            print("Invalid time input. Please enter a number.")

    adjust_srt_timing(input_file, action, time_adjustment)
