import pygame
import random
import importlib
from settings import *
from functions import *

player1 = importlib.import_module("players." + PLAYER_1_NAME)
player2 = importlib.import_module("players." + PLAYER_2_NAME)
players = [PLAYER_1_NAME, PLAYER_2_NAME]
turn = 0

# initialize pygame and create window
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
font = pygame.font.SysFont(TEXT_FONT, TEXT_SIZE)

# define player tables
player1_table = [[" " for j in range(0, TABLE_WIDTH)] for i in range(0, TABLE_HEIGHT)] 
player2_table = [[" " for j in range(0, TABLE_WIDTH)] for i in range(0, TABLE_HEIGHT)]
table = [[" " for j in range(0, TABLE_WIDTH)] for i in range(0, TABLE_HEIGHT)]

# Game loop
running = True
close = False
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
            close = True

    # Update

    # check if we have a winner
    winner = get_winner(table)
    if winner is not None:
        write(screen, font, (10, HEIGHT - 40), BLACK, players[(turn + 1) % 2] + " won as " + winner)
        pygame.display.flip()
        break

    # check if we table is full
    if table_is_full(table):
        write(screen, font, (10, HEIGHT - 40), BLACK, "Tie!")
        pygame.display.flip()
        break
    if turn:
        # player 2's turn
        try:
            for i in range(0, TABLE_HEIGHT):
                for j in range(0, TABLE_WIDTH):
                    if table[i][j] == "O":
                        player2_table[i][j] = "X"
                    elif table[i][j] == "X":
                        player2_table[i][j] = "O"
                    else:
                        player2_table[i][j] = " "
            row, column = player2.get_move(player2_table)
            if check_move(table, row, column):
                table[row][column] = "O"
            else:
                print(PLAYER_2_NAME, "false move\n")
        except Exception as e:
            print(PLAYER_2_NAME, "error:\n", e, "\n")

    else:
        # player 1's turn
        try:
            for i in range(0, TABLE_HEIGHT):
                for j in range(0, TABLE_WIDTH):
                    player1_table[i][j] = table[i][j]
            row, column = player1.get_move(player1_table)
            if check_move(table, row, column):
                table[row][column] = "X"
            else:
                print(PLAYER_1_NAME, "false move\n")
        except Exception as e:
            print(PLAYER_1_NAME, "error:\n", e, "\n")
    turn = (turn + 1) % 2

    # Draw / render
    screen.fill(WHITE)
    draw_table(screen, table)
    write(screen, font, (10, 10), BLACK, "X is " + PLAYER_1_NAME)
    write(screen, font, (10, 40), BLACK, "O is " + PLAYER_2_NAME)
    # write(screen, font, (10, 70), BLACK, players[turn] + "'s turn")

    # *after* drawing everything, flip the display
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)

if close:
    pygame.quit()
    exit()
else:
    while running:
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
    exit()
