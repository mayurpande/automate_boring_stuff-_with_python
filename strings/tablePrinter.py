#! /usr/bin/python3

#tablePrinter.py - A program to print a list of strings in a 
#well organized table with each column right-justified


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable():
	temp = 0
	for i in range(len(tableData)):
		for j in range(len(tableData[i])):
			if temp < (len(tableData[i][j])):
				temp = len(tableData[i][j])
			else:
				continue
	
	
	for j in range(len(tableData[0])):
		for i in range(len(tableData)):
			print(tableData[i][j].rjust(temp),end='')
		print()

printTable()					 
