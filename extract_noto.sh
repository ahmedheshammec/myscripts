#!/bin/bash

# Function to display usage information
usage() {
    echo "Usage: $0 <directory>"
    exit 1
}

# Check if a directory was provided as an argument
if [ -z "$1" ]; then
    echo "Error: No directory provided."
    usage
fi

# Check if the provided argument is a valid directory
if [ ! -d "$1" ]; then
    echo "Error: The provided path is not a valid directory."
    usage
fi

# Get the directory path from the argument
DIR="$1"

# Move all files and subdirectories one level up
mv "$DIR"/* "$DIR"/../

# Check if the move was successful
if [ $? -eq 0 ]; then
    # Remove the original directory
    rm -r "$DIR"
    echo "Files moved and directory '$DIR' deleted successfully."
else
    echo "Error: Failed to move files."
    exit 1
fi