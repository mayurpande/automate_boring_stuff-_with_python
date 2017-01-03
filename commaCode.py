def commaCode(arr):
	st = ""
	end = arr[-1]
	start = arr[0:-1]
	for i in range(len(start)):
		if isinstance(start[i],int):
			st += str(start[i]) + ", "
		else:
			st += start[i] + ", "

	if isinstance(start[i],int):
		print(st + "and " + str(end))
	else:
		print(st + "and " + end)
		
		
		

spam = [1,'t','g','d']
commaCode(spam)	
