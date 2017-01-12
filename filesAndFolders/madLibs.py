#! /usr/bin/python3

# madLibs.py program that reads in text files and lets
# users add their own text anywhere the word 
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

def openReadFile():
	madLibs = open('/home/mayur/environements/automate_boring_stuff_with_python/filesAndFolders/madLibs.txt','w')

	madLibs.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')

	madLibs.close()
	madLibs = open('madLibs.txt')
	content = madLibs.read()
	madLibs.close()
	print(content)

def displayContent():
	print('Enter an adjective:\n')
	adjective = input()
	print('Enter a noun:\n')
	noun = input()
	print('Enter a verb\n')
	verb = input()
	print('Enter a noun:\n')
	noun2 = input()
	localWordList = [adjective, noun, verb, noun2]
	return localWordList

def changeText(wordList):
	#open and read from file
    madLibs = open('madLibs.txt')
	content = madLibs.read()

	#use regex to search and replace content

	#save to new text file
    


changeText(displayContent())
	
