theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']) 
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])   


	
def checkWin(turn):
	 if(((theBoard['top-L']==turn && theBoard['top-M']==turn && theBoard['top-R']==turn)||
    (theBoard['mid-L']==turn && board['mid-M']==turn && theBoard['mid-R']==turn)||
    (theBoard['low-L']==turn && board['low-M']==turn && theBoard['low-R']==turn)||
	(theBoard['top-L']==turn && board['mid-L']==turn && theBoard['low-L']==turn)||
	(theBoard['top-M']==turn && board['mid-M']==turn && theBoard['low-M']==turn)||
	(theBoard['top-R']==turn && board['mid-R']==turn && theBoard['low-R']==turn)||
	(theBoard['top-R']==turn && board['mid-M']==turn && theBoard['low-L']==turn)||
	(theBoard['top-L']==turn && board['mid-M']==turn && theBoard['low-R']==turn)||





)))
		

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
		checkWin(turn)
		printBoard(theBoard)


makeMove()
