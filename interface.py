# in this file will be the interface of the game
# here are defined buttons class and color gradients function

import pygame
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

def normalize(color):
    # normalize color from 0-255 range to 0-1 range
    return tuple(x/255 for x in color)

def denormalize(color):
    # denormalize color from 0-1 range to 0-255 range
    return tuple(int(255*x) for x in color[:3])

def get_nice_gradient(N):
    """
    Generate a list of N colors forming a gradient with used colors by using matplotlib

    Args:
        N (int): number of colors to generate

    Returns:
        list: list of N colors as (r, g, b) tuples in range 0-255
    """
    ORANGE = (255, 204, 153)
    BLUE = (40, 64, 92)
    LIGHTBLUE = (66, 137, 155)
    AQUA = (148, 196, 193)
    GREEN = (197, 204, 130)
    TIDAL = (224, 238, 163)
    BEIGE = (227, 195, 157)
    LIGHTPINK = (249, 199, 190)
    PINK = (228, 166, 157)
    RED = (206, 106, 108)
    DARKRED = (68, 12, 30)
    BLACK = (0, 0, 0)
    DARKBLUE = (27, 48, 73)
    colors = list(map(lambda x: normalize(x), [BEIGE, TIDAL, GREEN, AQUA, LIGHTBLUE, AQUA, BEIGE, ORANGE, LIGHTPINK, PINK, RED, DARKRED, BLACK, DARKBLUE, BLUE]))

    cmap = LinearSegmentedColormap.from_list('nice_gradient', colors, N=N)
    return [denormalize(cmap(i)) for i in np.linspace(0, 1, N)]


class Button:

    def __init__(self, size, location, color, text=None):
        """
        Initialize a button
        args:
            size - (width, height) of the button
            location - (x, y) coordinates of the top left corner of the button
            color - (r, g, b) color of the button
            text - text to display on the button
        """
        # w - width, h - height
        self.w, self.h = size[0], size[1]
        # coordinates of top left corner
        self.x, self.y = location[0], location[1]
        self.color = color
        self.text = text
        self.rectangle = pygame.Rect(self.x, self.y, self.w, self.h)

    def move(self, delta_x, delta_y):

        self.x += delta_x
        self.y += delta_y
        self.rectangle = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, screen, text_color=(0, 0, 0)):
        """draw the button (rectangle with rounded corners) on the screen

        Args:
            screen (pygame.display.set_mode(w, h)): pygame display surface
            text_color (tuple, optional): color of the text. Defaults to (0, 0, 0).
        """
        rectangle = pygame.draw.rect(screen, self.color, self.rectangle, border_radius=2)
        text_surface_object = pygame.font.SysFont(None, 30).render(
                    self.text, True, text_color)
        text_rect = text_surface_object.get_rect(center=rectangle.center)
        screen.blit(text_surface_object, text_rect)
