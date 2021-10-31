import pygame
from settings import *

def draw_table(screen, table):
    start = (TABLE_TOP_LEFT_CORNER[0], TABLE_TOP_LEFT_CORNER[1] + CELL_WIDTH)
    end = (TABLE_BOTTOM_RIGHT_CORNER[0], TABLE_TOP_LEFT_CORNER[1] + CELL_WIDTH)
    pygame.draw.line(screen, BLACK, start, end, 1)

    start = (TABLE_TOP_LEFT_CORNER[0], TABLE_TOP_LEFT_CORNER[1] + CELL_WIDTH * 2)
    end = (TABLE_BOTTOM_RIGHT_CORNER[0], TABLE_TOP_LEFT_CORNER[1] + CELL_WIDTH * 2)
    pygame.draw.line(screen, BLACK, start, end, 1)

    start = (TABLE_TOP_LEFT_CORNER[0] + CELL_WIDTH, TABLE_TOP_LEFT_CORNER[1])
    end = (TABLE_TOP_LEFT_CORNER[0] + CELL_WIDTH, TABLE_BOTTOM_RIGHT_CORNER[1])
    pygame.draw.line(screen, BLACK, start, end, 1)

    start = (TABLE_TOP_LEFT_CORNER[0] + CELL_WIDTH * 2, TABLE_TOP_LEFT_CORNER[1])
    end = (TABLE_TOP_LEFT_CORNER[0] + CELL_WIDTH * 2, TABLE_BOTTOM_RIGHT_CORNER[1])
    pygame.draw.line(screen, BLACK, start, end, 1)

    for i in range(0, TABLE_HEIGHT):
        for j in range(0, TABLE_WIDTH):
            if table[i][j] == "X":
                start = (
                    TABLE_TOP_LEFT_CORNER[0] + j * CELL_WIDTH + 5,
                    TABLE_TOP_LEFT_CORNER[1] + i * CELL_WIDTH + 5 
                )
                end = (
                    TABLE_TOP_LEFT_CORNER[0] + (j + 1) * CELL_WIDTH - 5,
                    TABLE_TOP_LEFT_CORNER[1] + (i + 1) * CELL_WIDTH - 5
                )
                pygame.draw.line(screen, BLACK, start, end, 1)
                start = (
                    TABLE_TOP_LEFT_CORNER[0] + (j + 1) * CELL_WIDTH - 5,
                    TABLE_TOP_LEFT_CORNER[1] + i * CELL_WIDTH + 5
                )
                end = (
                    TABLE_TOP_LEFT_CORNER[0] + j * CELL_WIDTH + 5,
                    TABLE_TOP_LEFT_CORNER[1] + (i + 1) * CELL_WIDTH - 5 
                )
                pygame.draw.line(screen, BLACK, start, end, 1)
            elif table[i][j] == "O":
                center = (
                    TABLE_TOP_LEFT_CORNER[0] + CELL_WIDTH / 2 + j * CELL_WIDTH,
                    TABLE_TOP_LEFT_CORNER[1] + CELL_WIDTH / 2 + i * CELL_WIDTH
                )
                pygame.draw.circle(screen, BLACK, center, (CELL_WIDTH // 2) - 5, width=1)

def write(screen, font, position, colour, text):
    textsurface = font.render(text, False, colour)
    screen.blit(textsurface, position)

def check_move(table, row, column):
    if table[row][column] != " ":
        return False
    else:
        return True

def table_is_full(table):
    for i in range(0, TABLE_HEIGHT):
        for j in range(0, TABLE_WIDTH):
            if table[i][j] == " ":
                return False
    return True

def get_winner(table):
    # check O
    # O O O
    for i in range(0, 3):
        if table[i][0] == "O":
            if table[i][1] == "O":
                if table[i][2] == "O":
                    return "O"
    # O
    # O
    # O
    for j in range(0, 3):
        if table[0][j] == "O":
            if table[1][j] == "O":
                if table[2][j] == "O":
                    return "O"
    # O
    #  O
    #   O
    if table[0][0] == "O":
        if table[1][1] == "O":
            if table[2][2] == "O":
                return "O"
    #   O
    #  O
    # O
    if table[2][0] == "O":
        if table[1][1] == "O":
            if table[0][2] == "O":
                return "O"
    # check X
    # X X X
    for i in range(0, 3):
        if table[i][0] == "X":
            if table[i][1] == "X":
                if table[i][2] == "X":
                    return "X"
    # X
    # X
    # X
    for j in range(0, 3):
        if table[0][j] == "X":
            if table[1][j] == "X":
                if table[2][j] == "X":
                    return "X"
    # X
    #  X
    #   X
    if table[0][0] == "X":
        if table[1][1] == "X":
            if table[2][2] == "X":
                return "X"
    #   X
    #  X
    # X
    if table[2][0] == "X":
        if table[1][1] == "X":
            if table[0][2] == "X":
                return "X"
    return None
