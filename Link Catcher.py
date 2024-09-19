#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
import time
import threading
import subprocess

# Set up Chrome WebDriver with DevTools Protocol enabled
options = Options()
options.add_argument("--start-maximized")
options.add_argument("user-data-dir=/Users/Ahmed/Library/Application Support/Google/Chrome/")  # Specify the path to your profile
options.add_argument("profile-directory=Default")  # Use the 'Default' profile (or 'Profile 1', etc.)
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})  # Enable performance logging

# Start a new Chrome session
driver = webdriver.Chrome(service=Service(), options=options)

# Open a website (e.g., Google)
driver.get("https://www.google.com")
print(driver.title)

capturing_links = False

def format_with_jq(data):
    """Uses jq to format JSON data."""
    try:
        # Run jq as a subprocess
        result = subprocess.run(['jq', '.'], input=json.dumps(data), text=True, capture_output=True)
        return result.stdout if result.returncode == 0 else json.dumps(data, indent=2)
    except Exception as e:
        print(f"Error formatting with jq: {e}")
        return json.dumps(data, indent=2)

def capture_links():
    """Captures download links from network logs."""
    try:
        logs = driver.get_log('performance')
        for log in logs:
            message = json.loads(log['message'])['message']

            if message.get('method') == 'Network.responseReceived':
                params = message.get('params', {})
                response = params.get('response', {})
                url = response.get('url')
                mime_type = response.get('mimeType')

                log_data = {
                    "type": "response",
                    "url": url,
                    "mimeType": mime_type
                }

                # Use jq to format the output
                formatted_log = format_with_jq(log_data)
                print(formatted_log)

            elif message.get('method') == 'Network.requestWillBeSent':
                params = message.get('params', {})
                request = params.get('request', {})
                url = request.get('url')

                log_data = {
                    "type": "request",
                    "url": url
                }

                # Use jq to format the output
                formatted_log = format_with_jq(log_data)
                print(formatted_log)

    except Exception as e:
        print(f"Error capturing links: {e}")


def start_capturing():
    """Starts the process to capture download links."""
    global capturing_links
    capturing_links = True
    print("Capturing download links. Press 't' to stop capturing.")
    
    while capturing_links:
        capture_links()
        time.sleep(1)  # Poll logs every second

def capture_in_thread():
    """Starts capturing in a new thread."""
    thread = threading.Thread(target=start_capturing)
    thread.start()

def stop_capturing():
    """Stops the capturing process."""
    global capturing_links
    capturing_links = False
    print("Stopped capturing download links.")

# Main loop: Press 'q' to quit, 'c' to capture links, and 't' to stop capturing
try:
    while True:
        if not capturing_links:
            command = input("Press 'q' to quit, 'c' to capture links: ").lower()
        else:
            command = input("Press 't' to stop capturing links: ").lower()

        if command == 'q' and not capturing_links:
            print("Closing browser session...")
            driver.quit()
            break
        elif command == 'c' and not capturing_links:
            capture_in_thread()  # Start capturing in a new thread
        elif command == 't' and capturing_links:
            stop_capturing()
        else:
            print("Invalid command.")
except KeyboardInterrupt:
    print("\nSession closed by user.")
    driver.quit()
