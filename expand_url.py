#!/usr/bin/env python3
# This Python Script Expands the Facebook Share Link to the Real Reel Link
import requests
import subprocess

def resolve_facebook_link(url):
    try:
        response = requests.get(url, allow_redirects=True)
        return response.url
    except requests.RequestException as e:
        print("Error resolving URL:", e)
        return None

def extract_base_url(url):
    try:
        # Use awk to extract the base URL before the '?'
        result = subprocess.run(f"echo {url} | awk -F'?' '{{print $1}}'", shell=True, check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Error extracting base URL:", e)
        return None

# Prompt the user to enter the Facebook share link
user_input_link = input("Please enter the Facebook share link: ")

# Pass the input link to the function
expanded_link = resolve_facebook_link(user_input_link)

if expanded_link:
    # Extract the base URL
    base_url = extract_base_url(expanded_link)
    print("Base URL:", base_url)
    
    if base_url:
        # Copy the base URL to the clipboard using pbcopy
        subprocess.run(f"echo {base_url} | pbcopy", shell=True)
        print("Base URL copied to clipboard.")