# tic-tac toe game self-made

import pandas as pd

def start_game():
    # Innitial communication with players

    size = int(input('Tic-Tac Toe game. What board sie do you want to play? (3,4,5): '))
    while not (size > 2 and size <= 5):
        
        size = int(input('Choose the correct size of the board (3,4,5): '))

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
        sign = (sign + 1) % 2
        print(f"\n{players[sign]}'s turn")
        try:
            column = int(input(f'Which column do you choose?: '))
        except ValueError:
            column = int(input(f'Choose correct column: '))

        row = int(input(f'Which row do you choose?: '))
        if board[column][row] not in players:
            board[column][row] = players[sign]
        else:
            print('This place is already taken')
        print(board)
        # player change
    game_on = input(f"Game over, {players[sign]} wins! Do you want to play again? (Y/N):")

    return game_on

def check_winner(player, board):
    is_winner = False
    z = board.shape[0]-1
    # check for columns:
    for column_name, column_data in board.items():
        if all(column_data.values == column_data.values[0]) and column_data.values[0] != '-':
            # print(f'Game over, the winner is {player}')
            is_winner = True
    # check for rows:
    # checks if rist element is the same like the rest
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