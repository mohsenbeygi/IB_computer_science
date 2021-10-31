import random
# you are X
def get_move(table):
    # row and column point to the cell of your move
    row = 0
    column = 0

    # the following code is an example code where you would play randomly
    available = []
    for i in range(0, 3):
        for j in range(0, 3):
            if table[i][j] == " ":
                available.append([i, j])

    number = random.randint(0, len(available) - 1)

    row = available[number][0]
    column = available[number][1]

    # ignore this:
    return row, column
