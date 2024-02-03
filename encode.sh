#!/bin/bash

# Get file path from argument 
filePath="$1"

# Extract file name and extension
fileName=$(basename "$filePath")
extension="${fileName##*.}"
fileName="${fileName%.*}"

# Rename original file to temp
mv "$filePath" "${filePath%/*}/temp.$extension" 

# Encode temp file
ffpb -i "${filePath%/*}/temp.$extension" -c:v libx264 -pix_fmt yuv420p -c:a aac "${filePath%/*}/${fileName}_output.$extension"

# Rename output file to original name
mv "${filePath%/*}/${fileName}_output.$extension" "$filePath"

# Delete temp file
rm "${filePath%/*}/temp.$extension"