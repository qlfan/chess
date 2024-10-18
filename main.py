import baseClasses
from pieces import *
from config import *
import pygame

pygame.init()

player1 = Player("Player 1", "white", 0)
player2 = Player("Player 2", "black", 0)

#Sets the board to its initial state
def config(board: Board, player1: Player, player2: Player):
    for i in range(8):
        board.board[6][i] = Pawn(6, i, player1, board)
        board.board[1][i] = Pawn(1, i, player2, board)

    board.board[7][0], board.board[7][7] = Rook(7, 0, player1, board), Rook(7, 7, player1, board)
    board.board[0][0], board.board[0][7] = Rook(0, 0, player2, board), Rook(0, 7, player2, board)

board = baseClasses.Board()

config(board, player1, player2)

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            pygame.draw.rect(board.screen, BROWN, pygame.Rect(i * WIDTH / 8, j * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))
        else:
            pygame.draw.rect(board.screen, TAN, pygame.Rect(i * WIDTH / 8, j * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))

pygame.display.flip()

#board.board[6][0] = Pawn(6, 0, None, board)

#board.display_board()

#clock = pygame.time.Clock()

running = True

while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Check for left mouse button input
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            
            #Find which square the player clicked
            row, col = int(pos[1] // (HEIGHT / 8)), int(pos[0] // (WIDTH / 8))
            print(f"It is {board.is_occupied(row, col)} that {row}, {col} is occupied")

    board.draw()
    pygame.display.flip()

pygame.display.quit()
pygame.quit()

"""honorable mentions
matty allen
"""