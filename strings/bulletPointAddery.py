#! /usr/bin/python3

# bullerPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

#paste text from clipboard
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):	#loop through all indexes in the "lines" list
	lines[i] = '* ' + lines[i] #add star to each string in "lines" list
text = '\n'.join(lines)
#copy the new text to the clipboard
pyperclip.copy(text) 
