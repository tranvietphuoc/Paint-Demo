import pygame
from settings import *


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PAINTING DEMO")


class Controller:
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, screen):
        x = self.rect.x
        y = self.rect.y
        width = self.rect.width
        height = self.rect.height
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        if self.text:
            controller_font = get_font(22)
            text_surface = controller_font.render(self.text, 1, self.text_color)
            screen.blit(text_surface, (x + width / 2 -
                text_surface.get_width()/2, y + height/2 - text_surface.get_height()/2))

    def clicked(self, pos):
        x, y = pos
        _x = self.rect.x
        _y = self.rect.y
        _width = self.rect.width
        _height = self.rect.height
        if not (x >= _x and x <= _x + _width):
            return False
        if not (y >= _y and y <= _y + _height):
            return False

        return True





def grid_init(rows, cols, color):
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid


def render_grid(screen, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(screen, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE,
                PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(screen, BLACK, (0, i * PIXEL_SIZE), (WIDTH,
                i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(screen, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE,
                HEIGHT - TOOLBAR_HEIGHT))


def draw(screen, grid, buttons):
    screen.fill(BG_COLOR)
    render_grid(screen, grid)

    for button in buttons:
        button.draw(screen)

    pygame.display.update()


def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError
    return row, col


run = True
clock = pygame.time.Clock()
grid = grid_init(ROWS, COLS, BG_COLOR)
draw_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT / 2 - 25
buttons = [
        Controller(10, button_y, 50, 50, BLACK),
        Controller(70, button_y, 50, 50, RED),
        Controller(130, button_y, 50, 50, GREEN),
        Controller(190, button_y, 50, 50, BLUE),
        Controller(250, button_y, 50, 50, WHITE, "Erase", BLACK),
        Controller(310, button_y, 50, 50, WHITE, "Clear", BLACK)
]

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = draw_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    draw_color = button.color
                    if button.text == "Clear":
                        grid = grid_init(ROWS, COLS, BG_COLOR)
                        draw_color = BLACK

    draw(SCREEN, grid, buttons)

pygame.quit()
