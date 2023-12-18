#!/bin/bash

location=$1
cd "$location"

# Ask for the video URL
read -p "Enter the video URL: " url

# Extract the title for the files
title=$(yt-dlp --get-filename -o "%(title)s" "$url")

# Download the best video
yt-dlp -f 'bestvideo[ext=mp4]' --output "${title}_video.mp4" "$url"

# Download the best audio
yt-dlp -f 'bestaudio[ext=m4a]' --output "${title}_audio.m4a" "$url"

# Check if the files exist
if [[ -f "${title}_video.mp4" ]] && [[ -f "${title}_audio.m4a" ]]; then
    echo "Files found. Proceeding with merge."
else
    echo "Files not found. Exiting."
    exit 1
fi

# Merge video and re-encode audio using ffpb
# Using H.264 video codec for better compatibility
ffpb -i "${title}_video.mp4" -i "${title}_audio.m4a" -c:v libx264 -c:a aac -b:a 128k -pix_fmt yuv420p "${title}.mp4"

# Clean up: Remove the temporary video and audio files
rm "${title}_video.mp4"
rm "${title}_audio.m4a"