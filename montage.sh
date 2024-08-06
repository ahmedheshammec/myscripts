#!/bin/bash

# Check if the project name is provided
if [ -z "$1" ]; then
    echo "Please provide a project name."
    exit 1
fi

# Get the current working directory
CURRENT_DIR=$(pwd)

# Define the project path
PROJECT_NAME="$1"
PROJECT_PATH="$CURRENT_DIR/$PROJECT_NAME.prproj"

# Copy the template to the new project location
cp /Users/Ahmed/Documents/Templates/basic_template.prproj "$PROJECT_PATH"
