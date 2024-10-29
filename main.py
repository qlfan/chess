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

def draw_grid():
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
stored_row, stored_col = -1, -1

while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Check for left mouse button input
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            #Find which square the player clicked
            if stored_row == -1 and stored_col == -1:
                stored_row, stored_col = int(pos[1] // (HEIGHT / 8)), int(pos[0] // (WIDTH / 8))
                if board.is_occupied(stored_row, stored_col):
                    selected_piece = board.board[stored_row][stored_col]
            
            #Equivalent to checking if a piece is selected
            elif stored_row != -1 and stored_col != -1:
                new_row, new_col = int(pos[1] // (HEIGHT / 8)), int(pos[0] // (WIDTH / 8))

                #This is a pretty ugly implementation I might make this more modular
                if board.board[stored_row][stored_col] != None:
                    if board.board[stored_row][stored_col].is_valid_move(stored_row, stored_col, new_row, new_col):
                        if board.is_turn(board.board[stored_row][stored_col].player):
                            #Verify that a piece can be captured if attempting to move to an occupied square
                            if board.is_occupied(new_row, new_col):
                                if board.board[new_row][new_col].player.piece_color != board.board[stored_row][stored_col].player.piece_color:
                                    board.board[stored_row][stored_col].kill()
                                    board.move_piece(stored_row, stored_col, new_row, new_col)
                                    board.switch_turn()
                            else:
                                board.board[stored_row][stored_col].kill()
                                board.move_piece(stored_row, stored_col, new_row, new_col)
                                board.switch_turn()

                stored_row, stored_col = -1, -1 

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print(stored_row, stored_col)
                

    draw_grid()
    board.draw()

    #DELETE THIS ONCE TURNS ARE VERIFIED TO WORK
    if board.turn_color == "white":
        pygame.draw.rect(board.screen, WHITE, pygame.Rect(WIDTH/2, HEIGHT/2, 20, 20))
    if board.turn_color == "black":
        pygame.draw.rect(board.screen, BLACK, pygame.Rect(WIDTH/2, HEIGHT/2, 20, 20))
    pygame.display.flip()

pygame.display.quit()
pygame.quit()

"""honorable mentions
matty allen
"""