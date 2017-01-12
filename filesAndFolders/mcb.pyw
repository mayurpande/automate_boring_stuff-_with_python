#! /usr/bin/python3

# mcb.pyw - Saves and Loads pieces of text to the clipboard.

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#		 py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyu list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
	
 #Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mchbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	#TODO: List keywords and load content

mcbShelf.close()


