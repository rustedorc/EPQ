import pygame
from os import path

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

#RGB
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 25)
WHITE_SQUARE = (235, 235, 208)
BLACK_SQUARE = (119, 148, 85)
GOLD = (255, 215, 0)

CROWN = pygame.transform.scale(pygame.image.load(path.join('assets', 'crown.png')), (44, 25))
