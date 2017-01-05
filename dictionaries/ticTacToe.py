theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']) 
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])   


	

		

def makeMove():
	turn = 'o'
	for i in range(9):
		print('Enter move for player ' + turn + ' for position on board')
		move = input()
		theBoard[move] = turn
		if turn == 'o':
			turn = 'x'
		else:
			turn = 'o'
		printBoard(theBoard)


makeMove()
