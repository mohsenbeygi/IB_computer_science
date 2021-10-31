import random
from settings import *

def get_move(table):
    # the following code choses a random cell
    # from the cells that are empty

    available = []
    for i in range(0, TABLE_HEIGHT):
        for j in range(0, TABLE_WIDTH):
            if table[i][j] == " ":
                available.append([i, j])

    number = random.randint(0, len(available) - 1)

    row = available[number][0]
    column = available[number][1]
    # print(available)

    return row, column