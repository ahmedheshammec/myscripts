#!/bin/bash

# Check if directory is provided as an argument
if [ $# -eq 1 ]; then
  DIRECTORY=$1
else
  DIRECTORY=$(pwd)
fi

# Check if directory is valid
if [ ! -d "$DIRECTORY" ]; then
  echo "Invalid directory"
  exit 1
fi

# Ask for input
read -p "Enter The Extensions You Want To Convert: " INPUT_EXTENSIONS
read -p "Enter The Extension You Want To Convert To: " OUTPUT_EXTENSION

# Split input extensions into an array
INPUT_EXTENSIONS_ARRAY=(${INPUT_EXTENSIONS//,/ })

# Loop through all files and sub-directories
find "$DIRECTORY" -type f -name "*.${INPUT_EXTENSIONS}" | while read file; do
  # Get file name without extension
  file_name=${file%.*}

  # Convert file based on output extension
  case $OUTPUT_EXTENSION in
    mp4)
      ffmpeg -y -nostdin -loglevel error -i "$file" -c:v libx264 -pix_fmt yuv420p "${file_name}.mp4"
      ;;
    mp3)
      ffmpeg -y -nostdin -loglevel error -i "$file" "${file_name}.mp3"
      ;;
    m4a)
      ffmpeg -y -nostdin -loglevel error -i "$file" "${file_name}.m4a"
      ;;
    *)
      echo "Unsupported output extension"
      exit 1
      ;;
  esac

  # Check if conversion was successful
  if [ $? -ne 0 ]; then
    echo "Error converting $file to $OUTPUT_EXTENSION"
    exit 1
  fi
done || {
  echo "Conversion interrupted"
  exit 1
}

echo "All files were converted successfully"

