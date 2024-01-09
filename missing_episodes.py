#!/usr/bin/env python3
import os
import re
import sys

def extract_episode_numbers(filename):
    """Extract episode numbers from filename using regex."""
    base_name = filename.split(".")[0]
    numbers = re.findall(r'\d+', base_name)
    return [int(num) for num in numbers]

# Check if folder path is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the folder path as a command-line argument.")
    sys.exit(1)

folder_path = sys.argv[1]

# Change the current working directory to the specified folder path
try:
    os.chdir(folder_path)
except FileNotFoundError:
    print("Folder not found.")
    sys.exit(1)

episode_set = set()

# Iterate through all files in the folder
for filename in os.listdir():
    if filename.endswith(".mp4"):
        episode_numbers = extract_episode_numbers(filename)
        episode_set.update(episode_numbers)

# Determine the range of episodes
if episode_set:
    all_episodes = sorted(episode_set)
    first_episode = all_episodes[0]
    last_episode = all_episodes[-1]
else:
    print("No episodes found.")
    sys.exit(1)

# Identify missing episodes
missing_episodes = [ep for ep in range(first_episode, last_episode + 1) if ep not in episode_set]

# Print the missing episodes
print("Missing episodes:")
for episode_number in missing_episodes:
    print(episode_number)