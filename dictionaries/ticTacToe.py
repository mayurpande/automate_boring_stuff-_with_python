theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

turn = 'O'
boardSize = 9
def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']) 
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])   


	
def checkWin():
	if (theBoard['top-L']==turn and theBoard['top-M']==turn and theBoard['top-R']==turn or theBoard['mid-L']==turn and board['mid-M']==turn and theBoard['mid-R']==turn) or (theBoard['low-L']==turn and theBoard['low-M']==turn and theBoard['low-R']==turn) or (theBoard['top-L']==turn and theBoard['mid-L']==turn and theBoard['low-L']==turn) or (theBoard['top-M']==turn and theBoard['mid-M']==turn and theBoard['low-M']==turn) or (theBoard['top-R']==turn and theBoard['mid-R']==turn and theBoard['low-R']==turn) or (theBoard['top-R']==turn and theBoard['mid-M']==turn and theBoard['low-L']==turn) or (theBoard['top-L']==turn and theBoard['mid-M']==turn and theBoard['low-R']==turn):
		return True
	else:
		return False
		

def makeMove():
	validInput = True
			
	while True:
		if turn == 'X':
			print('Player X enter your move:')
			move = input()
			if theBoard[move] == turn:
				print('Error move')
				continue
			else: 
				theBoard[move] = turn
				break
					
			
		elif turn == 'O':
			print('Player O enter your move:')
			move = input()
			if theBoard[move] == turn:
				print('Error move')
				continue
			else: 
				theBoard[move] = turn
				break
		
		
		
			


def changeMove():
	global turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
	


for i in range(boardSize):
	changeMove()
	makeMove()
	printBoard(theBoard)
	
