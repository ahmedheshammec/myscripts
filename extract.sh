#!/bin/bash

# Check if a directory path was provided
if [ -z "$1" ]; then
  echo "Usage: $0 <path to directory>"
  exit 1
fi

# The directory to search
SEARCH_DIR=$1

# Calculate the destination directory as one level up from the provided directory
DEST_DIR=$(dirname "$SEARCH_DIR")

# Find all files within the specified directory and its subdirectories
# and move them to the destination directory
find "$SEARCH_DIR" -type f -exec mv {} "$DEST_DIR" \;

echo "All files have been moved to $DEST_DIR"
