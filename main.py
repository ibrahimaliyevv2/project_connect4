import numpy as np

count_rows = 6
count_cols = 7

board = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])


def print_board():
    for row in range(0, count_rows):
        for col in range(0, count_cols):
            print(board[row][col], end=' ')
        print(" ")


def fill_in(col, player):
    col = col - 1
    for row in range(count_rows - 1, -1, -1):
        if board[row][col] == 0:
            print('legal move')
            board[row][col] = player
            break


def horizontal_win():
    for row in range(0, count_rows):
        for col in range(0, 4):
            if board[row][col] > 0:
                if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
                    print('Player', board[row][col], 'won!')
                    return True
    return False


def vertical_win():
    for row in range(0, 3):
        for col in range(0, count_cols):
            if board[row][col] > 0:
                if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]:
                    print('Player', board[row][col], 'won!')
                    return True
    return False


def diagonal_win():
    for row in range(3, count_rows):
        for col in range(0, 4):
            if board[row][col] > 0:
                if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]:
                    print('Player', board[row][col], 'won!')
                    return True
    for row in range(0, 3):
        for col in range(0, 4):
            if board[row][col] > 0:
                if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                    print('Player', board[row][col], 'won!')
                    return True
    return False


def win():
    if horizontal_win() or vertical_win() or diagonal_win():
        return True
    return False


player = 1
while not win():
    r = input('Enter a column: ')
    if r.isdigit() and 0 < int(r) < 8:
        fill_in(int(r), player)
        print_board()
        if player == 1:
            player = 2
        else:
            player = 1
    else:
        print('illegal move')
