#!/bin/bash
Location=$1
cd $Location
# Create a new directory named 'png'
mkdir -p png

# Convert all .psd files to .png and move them to the jpg directory
for file in *.psd; do
    if [ -f "$file" ]; then
        convert "$file[0]" -set filename:base "%[basename]" "png/%[filename:base].png"
    fi
done