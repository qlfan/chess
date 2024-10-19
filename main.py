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

    board.board[7][1], board.board[7][6] = Knight(7, 1, player1, board), Knight(7, 6, player1, board)
    board.board[0][1], board.board[0][6] = Knight(0, 1, player2, board), Knight(0, 6, player2, board)

    board.board[7][2], board.board[7][5] = Bishop(7, 2, player1, board), Bishop(7, 5, player1, board)
    board.board[0][2], board.board[0][5] = Bishop(0, 2, player2, board), Bishop(0, 5, player2, board)

    board.board[7][3] = Queen(7, 3, player1, board)
    board.board[0][3] = Queen(0, 3, player2, board)

    board.board[7][4] = King(7, 4, player1, board)
    board.board[0][4] = King(0, 4, player2, board)

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