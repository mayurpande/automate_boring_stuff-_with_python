#! /usr/bin/python3

# mcb.pyw - Saves and Loads pieces of text to the clipboard.

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#		 py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyu list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
	
 #Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
#delete keyword from the shelf
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	
	del mcbShelf[sys.argv[2]]
	
elif len(sys.argv) == 2:
	# List keywords and load contnt
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()


