#!/bin/bash
location=$1
cd "$location" || exit 1

# Script name
script_name="convert.sh"

mkdir -p converted

read -p "Enter The Extension You Want To Convert To: " ext_input

# Skip the script file
file_count=0
for file in *; do
    if [ "$file" = "$script_name" ]; then
        continue
    fi

    if [ "$ext_input" == "mp4" ]; then
        output_file="converted/${file%.*}.mp4"
        ffpb -i "$file" -c:v libx264 -pix_fmt yuv420p -c:a aac "$output_file" && {
            echo "Conversion successful: $output_file"
            rm "$file"
            echo "Removed original file: $file"
            ((file_count++))
        }

    elif [ "$ext_input" == "m4a" ]; then
        output_file="converted/${file%.*}.m4a"
        ffpb -i "$file" -c:a aac "$output_file" && {
            echo "Conversion successful: $output_file"
            rm "$file"
            echo "Removed original file: $file"
            ((file_count++))
        }
    
    elif [ "$ext_input" == "mp3" ]; then
        output_file="converted/${file%.*}.mp3"
        ffpb -i "$file" -c:a libmp3lame "$output_file" && {
            echo "Conversion successful: $output_file"
            rm "$file"
            echo "Removed original file: $file"
            ((file_count++))
        }
    fi
done

if [ $file_count -eq 0 ]; then
    echo "No files to convert. All Files Converted!"
else
    echo "$file_count file(s) converted."
fi

# Cleaning Up
cd converted || exit 1
mv * ../
cd ..
rm -r converted
echo "Cleaning Done!"
