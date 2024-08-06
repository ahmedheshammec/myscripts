#!/bin/bash

# Check if a directory path is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <directory-path>"
  exit 1
fi

# Change to the specified directory
cd "$1" || exit

# Create the 1080 directory if it doesn't exist
mkdir -p 1080

# Loop through all MP4 files in the current directory
for file in *.MP4; 
do
  # Check if there are no MP4 files in the directory
  if [ ! -e "$file" ]; then
    echo "No MP4 files found in the directory."
    exit 1
  fi
  
  # Get the base name of the file
  base_name=$(basename "$file" .mp4)
  
  # Convert the file using ffpb
  ffpb -i "$file" -pix_fmt yuv420p -c:v libx264 -c:a aac -vf scale=iw/2:ih/2 "1080/${base_name}_1080.mp4"
done

echo "Conversion complete."