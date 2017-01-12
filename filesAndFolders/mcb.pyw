#! /usr/bin/python3

# mcb.pyw - Saves and Loads pieces of text to the clipboard.

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#		 py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyu list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
	
 #TODO: Save clipboard content

 #TODO: List keywords and load content

mcbShelf.close()


