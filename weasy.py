#!/usr/bin/env python3
# To Use the the Script Open the Terminal and Cd to the Main Directory and Then Type `weasy.py .`

import os
import sys
from weasyprint import HTML

def convert_html_to_pdf(directory):
    html_files_found = False
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_files_found = True
                html_path = os.path.join(root, file)
                pdf_path = os.path.splitext(html_path)[0] + '.pdf'
                
                try:
                    html = HTML(filename=html_path)
                    html.write_pdf(pdf_path)
                    print(f"Converted: {html_path} -> {pdf_path}")
                except Exception as e:
                    print(f"Error converting {html_path}: {str(e)}")
    
    if not html_files_found:
        print(f"No HTML files found in {directory} or its subdirectories.")

if __name__ == "__main__":
    print(f"Arguments received: {sys.argv}")
    
    if len(sys.argv) != 2:
        print("Usage: weasy.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    print(f"Directory argument: {directory}")
    
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)

    print(f"Converting HTML files in {directory} and its subdirectories...")
    convert_html_to_pdf(directory)
    print("Script execution completed.")