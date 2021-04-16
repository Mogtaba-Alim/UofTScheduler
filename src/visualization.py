"""This file  is the visualization file for the UofTScheduler program"""
from typing import Union
import pygame
from pygame.colordict import THECOLORS
from week import Week
from day import Day


def initialize_screen(allowed: list) -> pygame.Surface:
    """Initialize pygame and the display window.

    allowed is a list of pygame event types that should be listened for while pygame is running.
    """
    pygame.display.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 700))
    screen.fill(THECOLORS['paleturquoise1'])
    pygame.display.flip()

    pygame.event.clear()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed([pygame.QUIT] + allowed)

    return screen


def draw_one_day_text(screen: pygame.Surface, day: Day, starting_width: Union[int, float]) -> None:
    """Draw the given text to the pygame screen at the given position.

    pos represents the *upper-left corner* of the text.
    """
    for i in range(len(day.get_subtree())):
        event = day.get_subtree()[i].return_root()[1]
        if event == "Empty":
            pass
        elif len(event) >= 19:
            event = event[:18]
            if event == '0:00':
                font = pygame.font.SysFont('inconsolata', 15)
                text_surface = font.render(event, True, THECOLORS['black'])
                width, height = text_surface.get_size()
                increment_height = screen.get_size()[1]
                pos = (starting_width + 5, (increment_height // 49) * 48)
                screen.blit(text_surface,
                            pygame.Rect(pos, (pos[0] + width, pos[1] + height)))
            else:
                font = pygame.font.SysFont('inconsolata', 15)
                text_surface = font.render(event, True, THECOLORS['black'])
                width, height = text_surface.get_size()
                increment_height = screen.get_size()[1]
                pos = (starting_width + 5, (i * (increment_height // 49)) + 12)
                screen.blit(text_surface,
                            pygame.Rect(pos, (pos[0] + width, pos[1] + height)))
        else:
            if event == '0:00':
                font = pygame.font.SysFont('inconsolata', 15)
                text_surface = font.render(event, True, THECOLORS['black'])
                width, height = text_surface.get_size()
                increment_height = screen.get_size()[1]
                pos = (starting_width + 5, (increment_height // 49) * 48)
                screen.blit(text_surface,
                            pygame.Rect(pos, (pos[0] + width, pos[1] + height)))
            else:
                font = pygame.font.SysFont('inconsolata', 15)
                text_surface = font.render(event, True, THECOLORS['black'])
                width, height = text_surface.get_size()
                increment_height = screen.get_size()[1]
                pos = (starting_width + 5, (i * (increment_height // 49)) + 12)
                screen.blit(text_surface,
                            pygame.Rect(pos, (pos[0] + width, pos[1] + height)))


def draw_time_slots(screen: pygame.Surface) -> None:
    """Draw the given text to the pygame screen at the given position.

    pos represents the *upper-left corner* of the text.
    """
    time_slots = [str(i // 2) + ":" + str(round(i % 2) * 3) + "0" for i in range(48)]
    for u in range(1, 48):
        font = pygame.font.SysFont('inconsolata', 15)
        text_surface = font.render(time_slots[u], True, THECOLORS['black'])
        width, height = text_surface.get_size()
        increment_height = screen.get_size()[1]
        y = ((u + 1) * (increment_height // 49)) + 5
        pos = (20, y)
        screen.blit(text_surface,
                    pygame.Rect(pos, (pos[0] + width, pos[1] + height)))


def draw_headings(screen: pygame.Surface) -> None:
    """Draw the given text to the pygame screen at the given position.

    pos represents the *upper-left corner* of the text.
    """
    font = pygame.font.SysFont('inconsolata', 20)
    for i in range(8):
        if i == 0:
            text_surface = font.render('Time', True, THECOLORS['black'])
            width, height = text_surface.get_size()
            screen.blit(text_surface,
                        pygame.Rect((10, 5), (10 + width, 5 + height)))
        else:
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            text_surface = font.render(days[i - 1], True, THECOLORS['black'])
            width, height = text_surface.get_size()
            width_increment = (screen.get_size()[0] - 50) // 7
            pos = (((i - 1) * width_increment) + 60, 5)
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
        if col == 1:
            pygame.draw.line(screen, color, (50, 0), (50, height))
        else:
            x = (col - 1) * ((width - 50) // 7) + 50
            pygame.draw.line(screen, color, (x, 0), (x, height))

    for row in range(1, 49):
        y = (row * (height // 49)) + 10
        if row == 1:
            pygame.draw.line(screen, color, (0, y), (width, y))
        else:
            pygame.draw.line(screen, color, (50, y), (width, y))


def draw_schedule(screen: pygame.surface, schedule: Week) -> None:
    """create the final schedule"""
    draw_grid(screen)
    draw_headings(screen)
    draw_time_slots(screen)
    width_increment = (screen.get_size()[1] // 7)
    increment_multiplier = 0
    for days in schedule.get_days():
        width = (width_increment * increment_multiplier) + 50
        draw_one_day_text(screen, days, width)


def visualize(schedule: Week) -> None:
    """Visualize the final schedule"""
    # Initialize the screen
    screen = initialize_screen([])

    while True:
        # Draw the list (on a pale turquoise background)
        screen.fill(THECOLORS['paleturquoise1'])
        draw_schedule(screen, schedule)
        pygame.display.flip()

        # Wait for an event (pygame.QUIT)
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            break

    pygame.display.quit()
