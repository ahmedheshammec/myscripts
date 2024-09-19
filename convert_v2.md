convert_v2.sh

```bash
#!/bin/bash

# Check if a directory was provided as a parameter
if [ -n "$1" ]; then
  cd "$1" || { echo "Invalid directory. Exiting."; exit 1; }
else
  cd "$(pwd)" || { echo "Failed to change directory. Exiting."; exit 1; }
fi

# Get the current directory
current_dir=$(pwd)

# Ask for the extensions to convert
read -p "Enter The Extensions You Want To Convert (comma-separated, e.g., mkv,mov): " input_extensions

# Convert the input string to an array
IFS=',' read -r -a input_ext_array <<< "$input_extensions"

# Ask for the extension to convert to
read -p "Enter The Extension You Want To Convert To: " output_extension

# Function to perform the conversion
convert_file() {
  local input_file="$1"
  local output_file="${input_file%.*}.$output_extension"

  if [ -f "$output_file" ]; then
    echo "Skipping conversion for $input_file as $output_file already exists."
  else
    case "$output_extension" in
      mp4)
        ffpb -i "$input_file" -c:v libx264 -pix_fmt yuv420p "$output_file"
        ;;
      mp3 | m4a)
        ffpb -i "$input_file" "$output_file"
        ;;
      *)
        echo "Unsupported output extension: $output_extension. Skipping."
        ;;
    esac
  fi
}

# Loop through all files and sub-directories
for ext in "${input_ext_array[@]}"; do
  find "$current_dir" -type f -name "*.$ext" | while IFS= read -r file; do
    convert_file "$file"
  done
done

# Print success message only after all conversions are complete
echo "All files were converted successfully."
```

