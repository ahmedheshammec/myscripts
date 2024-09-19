#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import time
import sys

def download_images(driver):
    # Find all image elements (This might need adjustment based on TikTok's HTML structure)
    images = driver.find_elements(By.TAG_NAME, 'img')

    # Create a directory to save images
    if not os.path.exists('tiktok_images'):
        os.makedirs('tiktok_images')

    # Download all images
    for index, img in enumerate(images):
        img_url = img.get_attribute('src')
        if img_url:
            img_name = f'image_{index}.jpeg'  # Create a file name
            img_data = requests.get(img_url).content
            
            with open(f'tiktok_images/{img_name}', 'wb') as handler:
                handler.write(img_data)
            
            print(f"Downloaded: {img_name}")

def main():
    # Get TikTok URL from user input
    url = input("Enter the TikTok URL: ")

    # Set up Selenium WebDriver (using the chromedriver from chromedriver-py)
    driver = webdriver.Chrome()

    # Open the TikTok page
    driver.get(url)

    while True:
        print("Press 'r' to retry downloading images or 'q' to quit.")
        user_input = input().strip().lower()

        if user_input == 'r':
            print("Retrying download...")
            download_images(driver)
        elif user_input == 'q':
            print("Quitting...")
            break
        else:
            print("Invalid input. Please press 'r' to retry or 'q' to quit.")

    # Close the WebDriver
    driver.quit()
    print("Download complete!")

if __name__ == "__main__":
    main()