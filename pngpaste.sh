#!/bin/bash

location=$1

# Check if the location starts with ~
if [[ "$location" == ~* ]]; then
    # Expand the path if it starts with ~
    eval location="$location"
fi

cd "$location" || { echo "Failed to change directory to $location"; exit 1; }
pngpaste image.png
