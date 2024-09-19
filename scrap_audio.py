#!/usr/bin/env python
import os
import json
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import browser_cookie3

def get_chrome_cookies(url):
    domain = url.split('/')[2]  # Extract domain from URL
    cookies = browser_cookie3.chrome(domain_name=domain)
    return [{'name': c.name, 'value': c.value, 'domain': c.domain, 'path': c.path} for c in cookies]

def add_cookies_to_driver(driver, cookies, url):
    driver.get(url)
    for cookie in cookies:
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"Couldn't add cookie {cookie['name']}: {str(e)}")
    driver.refresh()

def detect_audio(driver):
    try:
        time.sleep(5)  # Give some time for audio to start playing

        audio_sources = []

        # Check for HTML5 audio elements
        audio_elements = driver.find_elements(By.TAG_NAME, 'audio')
        for audio in audio_elements:
            src = audio.get_attribute('src')
            if src:
                audio_sources.append(("HTML5 Audio", src))

        # Check for video elements (which might contain audio)
        video_elements = driver.find_elements(By.TAG_NAME, 'video')
        for video in video_elements:
            src = video.get_attribute('src')
            if src:
                audio_sources.append(("Video", src))

        # Execute JavaScript to find playing media
        playing_media = driver.execute_script("""
            var media = document.querySelectorAll('audio, video');
            var playing = [];
            for (var i = 0; i < media.length; i++) {
                if (!media[i].paused) {
                    playing.push(media[i].src);
                }
            }
            return playing;
        """)
        
        for src in playing_media:
            audio_sources.append(("Playing Media", src))

        return audio_sources

    except Exception as e:
        print(f"An error occurred while detecting audio: {str(e)}")
        return []

def download_audio(url, output_file):
    command = [
        'curl', '-#', '-L', '-o', output_file, 
        '-H', 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        url
    ]
    subprocess.run(command, check=True)

def main():
    chrome_options = Options()
    chrome_options.add_argument("--autoplay-policy=no-user-gesture-required")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        while True:
            # Get URL from user input
            url = input("Enter the TikTok URL (or 'q' to quit): ")
            if url.lower() == 'q':
                break

            # Get cookies from Chrome
            cookies = get_chrome_cookies(url)
            
            # Add cookies to the driver and navigate to the URL
            add_cookies_to_driver(driver, cookies, url)

            while True:
                # Detect audio sources
                audio_sources = detect_audio(driver)

                if audio_sources:
                    print("Detected audio sources:")
                    for i, (source_type, source_url) in enumerate(audio_sources, 1):
                        print(f"{i}. {source_type}: {source_url}")

                    # Ask user which source to download
                    choice = input("Enter the number of the source you want to download (0 to skip, r to retry detection): ")
                    if choice.lower() == 'r':
                        print("Retrying audio detection...")
                        continue
                    choice = int(choice)
                    if 0 < choice <= len(audio_sources):
                        _, download_url = audio_sources[choice - 1]
                        output_file = "downloaded_audio.mp3"
                        print(f"Downloading audio from {download_url}")
                        download_audio(download_url, output_file)
                        print(f"Audio downloaded as {output_file}")
                    elif choice != 0:
                        print("Invalid choice. Skipping download.")
                    break
                else:
                    retry = input("No audio sources detected. Enter 'r' to retry or any other key to go back to URL input: ")
                    if retry.lower() != 'r':
                        break
                    print("Retrying audio detection...")

    except KeyboardInterrupt:
        print("\nScript terminated by user.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Close the WebDriver
        driver.quit()

    print("Audio detection and download complete!")

if __name__ == "__main__":
    main()