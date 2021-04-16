from typing import Tuple
from tkinter import *

import pygame
from pygame.colordict import THECOLORS
from week import Week


def initialize_screen(allowed: list) -> pygame.Surface:
    """Initialize pygame and the display window.

    allowed is a list of pygame event types that should be listened for while pygame is running.
    """
    pygame.display.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 700))
    screen.fill(THECOLORS['white'])
    pygame.display.flip()

    pygame.event.clear()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed([pygame.QUIT] + allowed)

    return screen


def draw_text(screen: pygame.Surface, text: str, pos: tuple[int, int]) -> None:
    """Draw the given text to the pygame screen at the given position.

    pos represents the *upper-left corner* of the text.
    """
    font = pygame.font.SysFont('inconsolata', 22)
    text_surface = font.render(text, True, THECOLORS['black'])
    width, height = text_surface.get_size()
    screen.blit(text_surface,
                pygame.Rect(pos, (pos[0] + width, pos[1] + height)))


def draw_grid(screen: pygame.surface) -> None:
    """Draws a square grid on the given surface.

    The drawn grid has GRID_SIZE columns and rows.
    You can use this to help you check whether you are drawing nodes and edges in the right spots.
    """
    color = THECOLORS['grey']
    width, height = screen.get_size()

    for col in range(1, 8):
        x = col * (width // 8)
        pygame.draw.line(screen, color, (x, 0), (x, height))

    for row in range(1, 49):
        if row == 1:
            y = (row * (height // 49)) + 10
            pygame.draw.line(screen, color, (0, y), (width, y))
        else:
            y = (row * (height // 49)) + 10
            first_column_width = width // 8
            pygame.draw.line(screen, color, (first_column_width, y), (width, y))

    pygame.display.flip()
    pygame.event.wait()
    pygame.display.quit()


def draw_schedule(Schedule: Week) -> None:
    """create the final schedule"""
    screen = initialize_screen([])

    for days in Schedule.get_days():
        for
