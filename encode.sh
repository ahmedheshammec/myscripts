#!/bin/bash

# Get file path from argument
filePath="$1"

# Extract file name and extension
fileName=$(basename "$filePath")
baseName="${fileName%.*}"

# Generate a random five-digit number
randomNumber=$(printf "%05d" $((RANDOM % 100000)))

# Create a temporary file name with random five digits for the output
tempFileName="temp_$randomNumber.mp4"
tempFilePath="${filePath%/*}/$tempFileName"

# Encode original file to the temporary file
ffpb -i "$filePath" -c:v libx264 -pix_fmt yuv420p -c:a aac "$tempFilePath"

# Check if the encoding was successful
if [ $? -eq 0 ]; then
    # Remove the original file
    rm "$filePath"
    
    # Rename the temporary file to the original filename with .mp4 extension
    mv "$tempFilePath" "${filePath%/*}/${baseName}.mp4"
    
    echo "Conversion successful. Original file removed and new file renamed."
else
    echo "Conversion failed. Original file untouched."
    rm "$tempFilePath"
fi