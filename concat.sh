#!/bin/bash

# Get the folder path from the command-line argument
location=$1

# Change directory to the specified folder
cd "$location" || exit

# Output file name
output_file="output.mp4"

# Create a temporary file list
list_file=$(mktemp)

# Iterate over each video file in the folder and save the file names to a list file
for video_file in *.mp4; do
  if [ -e "$video_file" ]; then
    echo "file '$PWD/$video_file'" >> "$list_file"
  fi
done

# Construct the FFmpeg command
ffmpeg_command=("ffmpeg")
ffmpeg_command+=("-f" "concat")
ffmpeg_command+=("-safe" "0")
ffmpeg_command+=("-i" "$list_file")
ffmpeg_command+=("-c:v" "copy")
ffmpeg_command+=("-c:a" "copy")
ffmpeg_command+=("$output_file")

# Execute the FFmpeg command
"${ffmpeg_command[@]}"

# Remove the temporary list file
rm "$list_file"
