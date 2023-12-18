#!/bin/bash
location=$1
cd "$location"

# Script name
script_name="convert.sh"

mkdir -p converted
file_count=0

for file in *; do
    # Skip the script file
    if [ "$file" = "$script_name" ]; then
        continue
    fi

    if [ -f "$file" ]; then
        output_file="converted/${file%.*}.mp4"
        if ffpb -i "$file" -c:v libx264 -pix_fmt yuv420p -c:a aac "$output_file"; then
            echo "Conversion successful: $output_file"
            rm "$file"
            echo "Removed original file: $file"
            ((file_count++))
        else
            echo "Conversion failed for $file. Check file format and codecs."
        fi
    fi
done

if [ $file_count -eq 0 ]; then
    echo "No files to convert. All Files Converted!"
else
    echo "$file_count files converted."
fi