#!/bin/bash

location=$1
cd "$location"

mkdir -p output
i=1

# Function to get the current clipboard content as PNG
get_clipboard_content() {
    osascript -e "the clipboard as «class PNGf»"
}

# Get the initial clipboard content
last_clipboard_content=$(get_clipboard_content)

echo "Starting the image saving process. Press Ctrl+C or the key '0' to stop."

while true; do
    # Listen for key press with a 1-second timeout
    read -t 1 -n 1 key
    
    # If "0" is pressed, exit the loop
    if [[ $key == "0" ]]; then
        echo "Exiting due to key press..."
        exit 0
    fi

    current_clipboard_content=$(get_clipboard_content)
    
    # If the clipboard content has changed, save it
    if [[ "$current_clipboard_content" != "$last_clipboard_content" ]]; then
        cd "$location/output" || exit 1  # Change back to the output directory
        pngpaste "image_$i.png"
        echo "Saved image_$i.png"
        i=$((i+1))
        last_clipboard_content=$current_clipboard_content
    fi
done
