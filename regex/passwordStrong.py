#! /usr/bin/python3

# passwordStrong.py - a program to make user input enter a strong password
# using regex, this must be 8 characters long, have at least on uppercase and
# one lower case and one digit


import re


while True:
	print('Please enter pw, must be 8 characters long and contain one digit, one uppercase letter, and one lowercase letter')
	pw = input()
	pwChecker = re.compile(r'(^\w+\d+$){8,}')
	mo = pwChecker.findall(pw)
	if len(mo) == 0:
		continue
	else:
		break

print('Welcome you have securely logged in!')

