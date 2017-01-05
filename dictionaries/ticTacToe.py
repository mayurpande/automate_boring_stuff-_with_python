theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']) 
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])   


	

def playerTurn(turn):
	if turn == 'x':
		turn == 'o'
	else:
		 turn == 'x'
		

def makeMove():
	for i in range(9):
		print('Enter move for player ' + turn + ' for position on board')
		move = input()
		theBoard[move] = turn
		playerTurn(turn)
		printBoard(theBoard)


makeMove()
