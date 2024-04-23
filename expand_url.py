#!/usr/bin/env python3
# This Python Script Expands the Facebook Share Link to the Real Reel Link
import requests

def resolve_facebook_link(url):
    try:
        response = requests.get(url, allow_redirects=True)
        return response.url
    except requests.RequestException as e:
        print("Error resolving URL:", e)
        return None

# Prompt the user to enter the Facebook share link
user_input_link = input("Please enter the Facebook share link: ")

# Pass the input link to the function
expanded_link = resolve_facebook_link(user_input_link)
print("Expanded Link:", expanded_link)
