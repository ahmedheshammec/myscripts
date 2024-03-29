#!/bin/bash

location=$1

# Expand the path
eval location=$location

cd "$location"

# Prompt for playlist URL
read -p "Enter playlist URL: " playlist_url

# Prompt for playlist name
read -p "Enter playlist name: " playlist_name

# Check if playlist name was entered
if [ -z "$playlist_name" ]; then
    echo "No playlist name entered. Exiting."
    exit 1
fi

# Create a new directory and enter it
mkdir -p "$playlist_name"
cd "$playlist_name"

# Stop script here without downloading videos
yt-dlp -f 'bestvideo[ext=mp4][height<=?1080]+bestaudio[ext=m4a]' --output "%(playlist_index)s.%(title)s.%(ext)s" --download-archive archive.txt "$playlist_url" 2>/dev/null

