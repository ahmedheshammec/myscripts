#!/bin/bash

location=$1

# Expand the path
eval location=$location

cd "$location"

# Loop through all mkv files in the directory
for mkvfile in *.mkv; do
    # Check if the file exists
    if [[ -f "$mkvfile" ]]; then
        # Use filename without extension for the SRT file
        base_name=$(basename "$mkvfile" .mkv)
        srtfile="${base_name}.srt"

        # Extract subtitle
        ffmpeg -i "$mkvfile" -map 0:s:0 "$srtfile"
    fi
done
