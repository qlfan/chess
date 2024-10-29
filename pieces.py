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
        if player.piece_color == "white":
            self.image = pygame.image.load(path.join(image_location, "white_pawn.png"))
            self.rect = self.image.get_rect()
        if player.piece_color == "black":
            self.image = pygame.image.load(path.join(image_location, "black_pawn.png"))
    
    def is_valid_move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:

        #Check if player attempts to move up 2 squares
        if self.player.piece_color == "white":
            if (self.move_count == 0) and (new_row == current_row - 2) and (new_col == current_col):
                return True
        
        if self.player.piece_color == "black":
            if (self.move_count == 0) and (new_row == current_row + 2) and (new_col == current_col):
                return True
        
        #Check if player attempts to move up 1 square
        if self.player.piece_color == "white":
            if (new_row == current_row - 1) and (new_col == current_col) and not(self.board.is_occupied(new_row, new_col)):
                return True

        if self.player.piece_color == "black":
            if (new_row == current_row + 1) and (new_col == current_col) and not(self.board.is_occupied(new_row, new_col)):
                return True
            
        
        #Check if player attempts to capture diagonally
        if self.player.piece_color == "white":
            if (self.board.is_occupied(new_row, new_col)) and (new_row == current_row - 1) and (abs(new_col - current_col) == 1):
                return True
            
        if self.player.piece_color == "black":
            if (self.board.is_occupied(new_row, new_col)) and (new_row == current_row + 1) and (abs(new_col - current_col) == 1):
                return True
        
        return False
    
class Rook(Piece, pygame.sprite.Sprite):
    def __init__(self, row: int, col: int, player: Player, board: Board):
        Piece.__init__(self, 'Rook', row, col, player, board)
        self.groups = [board.all_sprites]
        pygame.sprite.Sprite.__init__(self, self.groups)
        if player.piece_color == "white":
            self.image = pygame.image.load(path.join(image_location, "white_rook.png"))
            self.rect = self.image.get_rect()
        if player.piece_color == "black":
            self.image = pygame.image.load(path.join(image_location, "black_rook.png"))

    def is_valid_move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:

        #Check that the move ends in the same row or column
        if (new_row == current_row) or (new_col == current_col):
            return True
        
        return False
    
class Bishop(Piece, pygame.sprite.Sprite):
    def __init__(self, row: int, col: int, player: Player, board: Board):
        Piece.__init__(self, 'Bishop', row, col, player, board)
        self.groups = [board.all_sprites]
        pygame.sprite.Sprite.__init__(self, self.groups)
        if player.piece_color == "white":
            self.image = pygame.image.load(path.join(image_location, "white_bishop.png"))
            self.rect = self.image.get_rect()
        if player.piece_color == "black":
            self.image = pygame.image.load(path.join(image_location, "black_bishop.png"))
    
    def is_valid_move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:

        #Check if move is diagonal
        if (abs(new_row - current_row) == abs(new_col - current_col)):
            return True
        
        return False

class Knight(Piece, pygame.sprite.Sprite):
    def __init__(self, row: int, col: int, player: Player, board: Board):
        Piece.__init__(self, 'Knight', row, col, player, board)
        self.groups = [board.all_sprites]
        pygame.sprite.Sprite.__init__(self, self.groups)
        if player.piece_color == "white":
            self.image = pygame.image.load(path.join(image_location, "white_knight.png"))
            self.rect = self.image.get_rect()
        if player.piece_color == "black":
            self.image = pygame.image.load(path.join(image_location, "black_knight.png"))

    def is_valid_move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:

        #Check for L shaped patterns
        if (abs(new_row - current_row) == 2) and (abs(new_col - current_col) == 1):
            return True
        
        #this is the ugliest comment of all time lol
        #Check for |¯¯¯¯  shapped patterns
        if (abs(new_row - current_row) == 1) and (abs(new_col - current_col) == 2):
            return True
        
        return False
    
class Queen(Piece,pygame.sprite.Sprite):
    def __init__(self, row: int, col: int, player: Player, board: Board):
        Piece.__init__(self, 'Queen', row, col, player, board)
        self.groups = [board.all_sprites]
        pygame.sprite.Sprite.__init__(self, self.groups)
        if player.piece_color == "white":
            self.image = pygame.image.load(path.join(image_location, "white_queen.png"))
            self.rect = self.image.get_rect()
        if player.piece_color == "black":
            self.image = pygame.image.load(path.join(image_location, "black_queen.png"))

    def is_valid_move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:
        #Check if move ends in the same row
        if ((new_row == current_row) and (new_col != current_col)):
            return self.board.is_valid_path(current_row, current_col, new_row, new_col, "horizontal")
        
        #Check if move ends in the same column
        if ((new_col == current_col) and (new_row != current_row)):
            return self.board.is_valid_path(current_row, current_col, new_row, new_col, "vertical")
        
        #Check if move is diagonal
        if (abs(new_row - current_row) == abs(new_col - current_col)):
            return True
        
        return False

class King(Piece, pygame.sprite.Sprite):
    def __init__(self, row: int, col: int, player: Player, board: Board):
        Piece.__init__(self, 'King', row, col, player, board)
        self.groups = [board.all_sprites]
        pygame.sprite.Sprite.__init__(self, self.groups)
        if player.piece_color == "white":
            self.image = pygame.image.load(path.join(image_location, "white_king.png"))
            self.rect = self.image.get_rect()
        if player.piece_color == "black":
            self.image = pygame.image.load(path.join(image_location, "black_king.png"))

    def is_valid_move(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:

        #Check that move is only one tile away
        if (abs(new_row - current_row) <= 1) and (abs(new_col - current_col) <= 1):
            return True
        return False