#!/bin/bash
Location=$1
cd $Location
# Create a new directory named 'jpg'
mkdir -p jpg

# Convert all .psd files to .jpg and move them to the jpg directory
for file in *.psd; do
    if [ -f "$file" ]; then
        convert "$file[0]" -set filename:base "%[basename]" "jpg/%[filename:base].jpg"
    fi
done