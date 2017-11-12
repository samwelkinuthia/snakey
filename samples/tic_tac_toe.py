board = {'tL':' ', 'tM':' ', 'tR':' ',
         'mL':' ', 'mM':' ', 'mR':' ',
         'bL':' ', 'bM':' ', 'bR':' '}

def print_board(n):
    print(n['tL'] + '|' + n['tM']+ '|'+ n['tR'])
    print('-+-+-')
    print(n['mL'] + '|' + n['mM']+ '|'+ n['mR'])
    print('-+-+-')
    print(n['bL'] + '|' + n['bM']+ '|'+ n['bR'])

turn = 'X'

print(
    "Welcome to tic tac toe.\nUse acronyms for spaces e.g. tL for top left, bM for bottom-middle and mR for middle-right :)")

for i in range(9):
    print_board(board)
    move = input('Turn for ' + turn + '. Move to Space?: ')
    if move in board:
        board[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    else:
        print("!!! ENTER A VALID BOARD COORDINATE!!!")

print_board(board)
