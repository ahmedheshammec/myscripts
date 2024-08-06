#!/bin/bash

# Get the path from the clipboard
path=$(pbpaste)

# Convert spaces to escaped spaces
converted_path=$(echo "$path" | sed 's/ /\\ /g')

# Print the converted path
echo "$converted_path"

# Copy the converted path to the clipboard
echo "$converted_path" | pbcopy