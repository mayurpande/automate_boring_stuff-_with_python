def commaCode(arr):
	st = ""
	end = arr[-1]
	start = arr[0:-1]
	for i in range(len(start)):
		if int(start[i]):
			st += str(start[i]) + ", "
		else:
			st += start[i] + ", "

	if int(start[i]) == True:
		print(st + "and " + str(end))
	else:
		print(st + "and " + end)
		
		
		

spam = ['test',2,3,4]
commaCode(spam)	
