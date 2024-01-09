#!/bin/bash

# This script will:

# 	1.	Create a new directory called jpg in the current directory.
# 	2.	Convert all .psd files in the current directory to .jpg and save them in the jpg directory.
# 	3.	Convert all .png files in the current directory to .jpg and save them in the jpg directory, then delete the original .png files.

Location=$1
cd "$Location"
# Create a new directory named 'jpg'
mkdir -p jpg

# Convert all .psd files to .jpg and move them to the jpg directory
for file in *.psd; do
    if [ -f "$file" ]; then
        convert "$file[0]" -set filename:base "%[basename]" "jpg/%[filename:base].jpg"
    fi
done

# Convert all .png files to .jpg and move them to the jpg directory, then delete the .png files
mogrify -path jpg -format jpg -background white -alpha remove -alpha off *.png && rm *.png