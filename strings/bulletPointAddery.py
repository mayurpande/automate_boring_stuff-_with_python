#! /usr/bin/python3

# bullerPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

#paste text from clipboard
text = pyperclip.paste()

# TODO:Separate lines and add stars

#copy the new text to the clipboard
pyperclip.copy(text) 
