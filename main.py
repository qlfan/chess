import baseClasses
from pieces import *
from config import *
import pygame

pygame.init()

board = baseClasses.Board()

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            pygame.draw.rect(board.screen, BROWN, pygame.Rect(i * WIDTH / 8, j * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))
        else:
            pygame.draw.rect(board.screen, TAN, pygame.Rect(i * WIDTH / 8, j * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))

pygame.display.flip()

board.board[6][0] = Pawn(6, 0, None, board)

board.display_board()

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    board.draw()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            row, col = int(pos[1] // (HEIGHT / 8)), int(pos[0] // (WIDTH / 8))
            print(f"It is {board.is_occupied(row, col)} that {row}, {col} is occupied")

"""honorable mentions
matty allen
"""