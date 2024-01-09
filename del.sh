#!/bin/bash

echo "Enter the name of the video file:"
read video_file

# Check if the file exists
if [ ! -f "$video_file" ]; then
    echo "File not found!"
    exit 1
fi

echo "Enter the start timestamp of the segment to be removed (format HH:MM:SS):"
read start_time

echo "Enter the end timestamp of the segment to be removed (format HH:MM:SS):"
read end_time

# Generate filenames for intermediate files
temp1="part1.mp4"
temp2="part2.mp4"
concat_list="concat_list.txt"

# Trim and re-encode the video
ffmpeg -i "$video_file" -to "$start_time" -c:v libx264 -c:a aac "$temp1"
ffmpeg -i "$video_file" -ss "$end_time" -c:v libx264 -c:a aac "$temp2"

# Create a list for concatenation
echo "file '$temp1'" > "$concat_list"
echo "file '$temp2'" >> "$concat_list"

# Concatenate the two parts
ffmpeg -f concat -safe 0 -i "$concat_list" -c copy output.mp4

# Clean up temporary files
rm "$temp1" "$temp2" "$concat_list"

echo "All Done!"