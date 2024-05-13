#!/usr/bin/env python3
import os
import shutil
import subprocess
import plistlib

def is_app_running(app_name):
    """Check if the application is currently running."""
    try:
        # This command returns the number of occurrences of the app in the process list
        result = subprocess.run(['pgrep', '-x', app_name], stdout=subprocess.PIPE)
        return result.stdout != b''  # Returns True if app is running
    except subprocess.CalledProcessError:
        return False  # pgrep returns non-zero exit status if no process found

def quit_app(app_name):
    """Quit the application using AppleScript."""
    subprocess.run(['osascript', '-e', f'tell app "{app_name}" to quit'])

def refresh_dock():
    """Refresh the Dock to update the icon changes."""
    subprocess.run(['killall', 'Dock'])

def change_icon(app_path, new_icon_path):
    # Path to the application's Info.plist
    plist_path = os.path.join(app_path, 'Contents', 'Info.plist')
    
    # Read the contents of Info.plist
    with open(plist_path, 'rb') as plist_file:
        plist_contents = plistlib.load(plist_file)
    
    # Find the icon file name
    icon_name = plist_contents.get('CFBundleIconFile', 'AppIcon')  # Default to 'AppIcon.icns' if not found
    if not icon_name.endswith('.icns'):
        icon_name += '.icns'
    
    # Full path to the current icon file
    current_icon_path = os.path.join(app_path, 'Contents', 'Resources', icon_name)
    
    # Backup the original icon (just in case)
    shutil.copy(current_icon_path, current_icon_path + '.bak')
    
    # Replace the current icon with the new icon
    shutil.copy(new_icon_path, current_icon_path)
    print(f"Icon replaced for {app_path.split('/')[-1]}")

    # Touch the app to update modification date
    subprocess.run(['touch', app_path])

    # Refresh the Dock
    refresh_dock()

# Main execution
if __name__ == "__main__":
    app_path = '/Applications/Visual Studio Code.app'
    new_icon_path = '/Users/Ahmed/Documents/icns/VS--Code.icns'
    app_name = 'Visual Studio Code'

    # Check if Brave is running and quit if it is
    if is_app_running(app_name):
        quit_app(app_name)
        print(f"{app_name} was running and has been quit.")

    change_icon(app_path, new_icon_path)
