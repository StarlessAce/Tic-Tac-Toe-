# tic-tac toe game self-made

import pandas as pd

def start_game():
    # Innitial communication with players
    print('Tic Tac Toe game')

    while True:
        try:
            size = int(input('Choose the size of the board (3,4,5): '))
            if size > 2 and size <= 5:
                break
        except ValueError:
            print('Choose the correct size of the board (3,4,5): ')

    # Creating a board (between 3 and 5 rows/columns)
    val = [''] * size
    for x in range(size):
        val[x] = ['-'] * size
    board = pd.DataFrame(val, index=[number + 1 for number in range(len(val))],
                         columns=[letter + 1 for letter in range(len(val))])
    print(board)
    players = ['x', 'o']
    sign = 0
    while not check_winner(players[sign], board):
        # player change
        sign = (sign + 1) % 2
        print(f"\n{players[sign]}'s turn")
        while True:
            try:
                column = int(input(f'Choose column: '))
                if column > 0 and column <= size:
                    break
                else:
                    print(f'The column number should be between 1 and {size}')
            except ValueError:
                print(f'The column number should be between 1 and {size}')

        while True:
            try:
                row = int(input(f'Choose row: '))
                if row > 0 and row <= size:
                    break
                else:
                    print(f'The row number should be between 1 and {size}')
            except ValueError:
                print(f'The row number should be between 1 and {size}')
        if board[column][row] not in players:
            board[column][row] = players[sign]
        else:
            print('This place is already taken')
        print(board)
        for column_name, column_data in board.items():
            if '-' in column_data.values:
                print('jest miejsce')
                no_winner = False
                break
            else:
                no_winner = True
            if no_winner == True:
                print('No winner')
                break

    game_on = input("Do you want to play again? (Y/N):")

    return game_on

def check_winner(player, board):
    is_winner = False
    z = board.shape[0] - 1

    # check for columns:
    for column_name, column_data in board.items():
        if all(column_data.values == column_data.values[0]) and column_data.values[0] != '-':
            # print(f'Game over, the winner is {player}')
            is_winner = True
    # check for rows:
    # checks if first element is the same like the rest
    x = board.eq(board.iloc[:, 0], axis=0).all(1)
    # checks if there is a " - " sign in a row (non-win situation for rows)
    y = board.iloc[:, 0] != '-'
    # checks two conditions above:
    rows_empty = x * y

    for row in rows_empty:
        if row:
            is_winner = True

    # check first diagonal:
    diag1 = []
    diag2 = []
    for i in range(0, board.shape[0]):
        diag1.append(board.iloc[i,i])
        diag2.append(board.iloc[z-i,i])
    if all(element == diag1[0] for element in diag1) and (diag1[0] != '-'):
        is_winner = True

    if all(element == diag2[0] for element in diag2) and (diag2[0] != '-'):
        is_winner = True

    return is_winner


# Game
game_on = start_game()
while game_on.upper() == 'Y':
    game_on = start_game()

print('End of the game')