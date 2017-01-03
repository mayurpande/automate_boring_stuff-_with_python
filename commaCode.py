def commaCode(arr):
	st = ""
	end = arr[-1]
	start = arr[0:-1]
	for i in range(len(start)):
		if int(start[i]):
			st += str(start[i]) + ", "

	if int(start[i]):
		print(st + "and " + str(end))
		
		
		

spam = [1,2,3,4]
commaCode(spam)	
