#!/usr/bin/env python3
import os
import sys
from PIL import Image

def upscale_image(input_image_path, output_image_path, scale_factor):
    with Image.open(input_image_path) as img:
        # Calculate the new size
        new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
        
        # Resize the image using LANCZOS filter
        upscaled_img = img.resize(new_size, Image.LANCZOS)
        
        # Save the upscaled image
        upscaled_img.save(output_image_path)

def upscale_directory(directory, scale_factor):
    # Create output directory based on the scale factor
    output_directory = os.path.join(directory, f"{scale_factor}x")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Check if the file is an image
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            output_image_path = os.path.join(output_directory, filename)
            # Upscale the image
            upscale_image(file_path, output_image_path, scale_factor)

def main():
    # Check if any arguments are passed
    if len(sys.argv) > 1:
        # If an image file is passed, skip asking for directory
        image_path = sys.argv[1]
        # Check if the file ends with supported image formats
        if image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            directory = os.path.dirname(image_path)
            scale_factor = float(input("Enter the multiplication factor: "))
            # Upscale the image
            upscale_image(image_path, os.path.join(directory, f"{scale_factor}x_{os.path.basename(image_path)}"), scale_factor)
        else:
            print("Unsupported file format. Please provide a valid image file.")
    else:
        # Ask for the directory to convert
        directory = input("Enter the directory to convert: ")
        # Ask for the multiplication factor
        scale_factor = float(input("Enter the multiplication factor: "))
        # Process the directory
        upscale_directory(directory, scale_factor)

if __name__ == "__main__":
    main()
