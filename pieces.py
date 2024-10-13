from baseClasses import *
from os import path
import pygame

game_location = path.dirname(__file__)
image_location = path.join(game_location, 'sprites')

class Pawn(Piece, pygame.sprite.Sprite):
    def __init__(self, row: int, col: int, player: Player, board: Board):
        Piece.__init__(self, 'Pawn', row, col, player, board)
        self.groups = [board.all_sprites]
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(path.join(image_location, "white_pawn.png"))
        self.rect = self.image.get_rect()
    
    def is_valid_move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:

        #Check if player attempts to move up 2 squares
        if (self.move_count == 0) and (new_row == current_row + 2) and (new_col == current_col):
            return True
        
        #Check if player attempts to move up 1 square
        elif (new_row == current_row + 1) and (new_col == current_col):
            return True
        
        #Check if player attempts to capture diagonally
        elif (self.board.is_occupied(new_row, new_col)) and (new_row == current_row + 1) and (abs(new_col - current_col) == 1):
            return True
        
        return False
    
class Rook(Piece):
    def __init__(self, row: int, col: int, player: Player, board: Board):
        super().__init__('Rook', row, col, player, board)

    def is_valid_move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:

        #Check that the move ends in the same row or column
        if (new_row == current_row) or (new_col == current_col):
            return True
        
        return False
    
class Bishop(Piece):
    def __init__(self, row: int, col: int, player: Player, board: Board):
        super().__init__('Bishop', row, col, player, board)
    
    def is_valid_move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:

        #Check if move is diagonal
        if (new_row != current_row) and (new_col != current_col):
            return True
        
        return False

class Knight(Piece):
    def __init__(self, row: int, col: int, player: Player, board: Board):
        super().__init__('Knight', row, col, player, board)
    
    def is_valid_move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:

        #Check for L shaped patterns
        if (abs(new_row - current_row) == 2) and (abs(new_col - current_col == 1)):
            return True
        
        #this is the ugliest comment of all time lol
        #Check for |¯¯¯  shapped patterns
        if (abs(new_row - current_row) == 1) and (abs(new_col - current_col == 2)):
            return True
        
        return False
    
class Queen(Piece):
    def __init__(self, row: int, col: int, player: Player, board: Board):
        super().__init__('Queen', row, col, player, board)
    
    def is_valid_move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:

        #Check that the move ends in the same row or column
        if (new_row == current_row) or (new_col == current_col):
            return True
        
        #Check if move is diagonal
        if (new_row != current_row) and (new_col != current_col):
            return True
        
        return False

class King(Piece):
    def __init__(self, row: int, col: int, player: Player, board: Board):
        super().__init__('King', row, col, player, board)

    def is_valid_move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:

        #Check that move is only one tile away
        pass