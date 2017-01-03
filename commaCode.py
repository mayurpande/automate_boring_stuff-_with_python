def commaCode(arr):
	st = ''
	end = arr[-1]
	start = arr[0:-1]
	for i in range(len(start)):
		st += start[i] + ", "

	print(st + "and " + end)
		
		
		

spam = [1,2,3,4]
commaCode(spam)	
