#! /usr/bin/python3

# madLibs.py program that reads in text files and lets
# users add their own text anywhere the word 
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.


madLibs = open('/home/mayur/environements/automate_boring_stuff_with_python/filesAndFolders/madLibs.txt','w')

madLibs.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')

madLibs.close()
madLibs = open('madLibs.txt')
content = madLibs.read()
madLibs.close()
print(content)
