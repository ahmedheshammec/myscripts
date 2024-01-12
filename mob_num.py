#!/usr/bin/env python3
import pyperclip

# Get the Text From the Clipboard
clipboard_text = pyperclip.paste()

# Removing Spaces with replace() Method
result = clipboard_text.replace(" ", "")

# Control result with if state and copy the output back to the clipboard
if result.startswith("+201"): 
    result = result.replace("+2", "")
    print(result)
    pyperclip.copy(result)
elif result.startswith("+200"):
    result = result.replace("+20", "")
    print(result)
    pyperclip.copy(result)
else: 
    print(result)
    pyperclip.copy(result)

