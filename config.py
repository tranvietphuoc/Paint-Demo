import pygame


# init
pygame.init()
pygame.font.init()

# colors
WHITE           = (255, 255, 255)
BLACK           = (0, 0, 0)
RED             = (255, 0, 0)
GREEN           = (0, 0, 255)
BLUE            = (0, 255, 0)
# fps
FPS             = 240
# another parameters
WIDTH, HEIGHT   = 600, 700
ROWS, COLS      = 100, 100
TOOLBAR_HEIGHT  = HEIGHT - WIDTH
PIXEL_SIZE      = WIDTH // COLS
BG_COLOR        = WHITE
DRAW_GRID_LINES = True


def get_font(size: int):
    return pygame.font.SysFont("comicsans", size)
