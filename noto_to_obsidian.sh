#!/bin/bash
# First Fix the Md Files Using the Find Command Before Running This Bash Script

# Check if a directory is provided as a parameter, if not use current directory
if [ -n "$1" ]; then
  target_dir="$1"
  cd "$target_dir" || { echo "Directory not found!"; exit 1; }
else
  target_dir=$(pwd)
fi

# Find all content.md files in the target directory and its subdirectories
find "$target_dir" -name 'content.md' | while read -r file; do
  # Extract the first line, clean it up, and use it as the new filename
  extracted_name=$(head -n 1 "$file" | sed 's/^[[:space:]#]*//')

  # Rename the file to the new name and remove the first line (the title)
  new_file_path="$(dirname "$file")/${extracted_name}.md"
  mv "$file" "$new_file_path"
  sed -i '' '1d' "$new_file_path"

  echo "Processed: $new_file_path"
done