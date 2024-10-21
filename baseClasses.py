import pygame
from config import *

class Player:
    def __init__(self, name: str, piece_color: str, score: int):
        self.name = name
        self.piece_color = piece_color
        self.score = score

#Game board
class Board:
    def __init__(self):
        self.board = [[None] * 8 for i in range(8)]
        self.all_sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    #Displays the board in text
    def display_board(self) -> None:
        for i in self.board:
            for j in i:
                print(j, end = '\t')
            print()

    #Moves a piece to a new square
    def move_piece(self, current_row: int, current_col: int, new_row: int, new_col: int) -> None:
        self.board[new_row][new_col] = self.board[current_row][current_col]
        self.board[new_row][new_col].row = new_row
        self.board[new_row][new_col].col = new_col
        self.board[new_row][new_col].move_count += 1
        self.remove_piece(current_row, current_col)
    
    #Removes a piece from the board
    def remove_piece(self, row: int, col: int) -> None:
        self.board[row][col] = None

    def is_occupied(self, row: int, col: int) -> bool:
        if self.board[row][col] != None:
            return True
        return False

    def draw(self):
        for row in self.board:
            for piece in row:
                if piece != None:
                    piece_type = piece.piece_type

                    #Finds the x and y positions that will center pieces
                    lower_x = piece.col * WIDTH / 8
                    upper_x = (piece.col + 1) * WIDTH / 8
                    x_diff = (upper_x - lower_x - 64) / 2 
                    lower_y = piece.row * HEIGHT / 8
                    upper_y = (piece.row + 1) * HEIGHT / 8
                    y_diff = (upper_y - lower_y - 64) / 2
                    self.screen.blit(piece.image, (lower_x + x_diff, lower_y + y_diff))
                    # match piece_type:
                    #     case 'Pawn':
                    #         self.screen.blit(piece.image, (lower_x + x_diff, lower_y + y_diff))



#Generic piece class
class Piece:
    def __init__(self, piece_type: str, row: int, col: int, player: Player, board: Board):
        self.piece_type = piece_type
        self.col = col
        self.row = row
        self.player = player
        self.board = board
        self.move_count = 0

    #Moves a piece to a new square if its path is valid
    def move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> None:
        if self.is_valid_move(current_row, current_col, new_row, new_col):
            self.board.move_piece(current_row, current_col, new_row, new_col)
            self.move_count += 1
        else:
            print('Invalid move')

    #Verifies that an attempted move is valid
    def is_valid_move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:
        pass