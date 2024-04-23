#!/bin/bash
# This Script Renames All Files Downloaded by yt-dlp in a Given Directory

# Function to rename a single file
rename_file() {
    local file="$1"
    # Use sed to remove the pattern [xxxx] including the preceding space
    newname=$(echo "$file" | sed 's/ \[.*\]//')
    # Rename the file
    mv "$file" "$newname"
}

# Check if the passed argument is a file or directory and rename accordingly
rename_argument() {
    local arg="$1"
    if [ -f "$arg" ]; then
        rename_file "$arg"
    elif [ -d "$arg" ]; then
        rename_directory "$arg"
    else
        echo "Invalid input: $arg is neither a file nor a directory."
    fi
}

# Function to rename all files in a directory
rename_directory() {
    local dir="$1"
    # Change directory to the specified directory
    cd "$dir" || { echo "Failed to change directory to $dir"; exit 1; }
    # Loop through all files in the directory
    for file in *; do
        if [ -f "$file" ]; then
            rename_file "$file"
        fi
    done
}

# Loop through all arguments passed to the script
for arg in "$@"; do
    rename_argument "$arg"
done
