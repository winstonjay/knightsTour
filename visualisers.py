import knightsTour as KT
import numpy as np
import time
import matplotlib.pyplot as plt

def display_tour(tour, size):

    def printboard(board):
        for row in board:
            print "-"*(size*5+1)
            print "".join(["| {:>2} ".format(col) for col in row]) + "|"
        print "-"*(size*5+1)

    board = [[" " for x in range(size)] for y in range(size)]
    for  i, z in enumerate(tour):
        x, y = z
        board[x][y] = i
        printboard(board)
        time.sleep(.5)

def plot_board(s, filter_fn, title):
    board = np.zeros((s,s,3))
    board += .85
    board[::2, ::2] = 1 # "White" color
    board[1::2, 1::2] = 1 # "White" color
    fig, ax = plt.subplots(figsize=(7,7))
    ax.imshow(board, interpolation='nearest')
    positions = [(x,y) for x in range(s) for y in range(s)]
    for x, y in positions:
        ax.text(x, y, filter_fn(x,y), size=15, ha='center', va='center')
    ax.set(xticks=[], yticks=[])
    ax.set_title(title, size="x-large")
    ax.axis('image')
    plt.show()

def chessName(square):
    """Converts vector co-ordinates to chess square names:
    squareName(0, 0) -> "a1"; squareName(7, 7) -> "h8"; """
    x, y = square
    return (chr(x + 97) + str(y+1))



