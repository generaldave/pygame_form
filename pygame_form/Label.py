'''
David Fuller

Label class for forms in Pygame

2017-9-30
'''

import pygame
import os.path

from collections import namedtuple

point = namedtuple('point', ['x', 'y'])
colour = namedtuple('colour', ['r', 'g', 'b'])
pygame.font.init()

class Label(object):
    '''
    Label class for forms in Pygame. Label value can be gotten with
    class.value.
    '''

    def __init__(self, screen,
                 value = '',
                 position = point(x = 0, y = 0),
                 font_family = 'Helvetica',
                 font_size = 20,
                 antialias = True,
                 text_colour = colour(r = 0, g = 0, b = 0)) -> None:
        '''
        init for Label class.

        screen = pygame.display
        value = str
        position = namedtuple('point', ['x', 'y'])
        font_family = ttf
        font_size = int
        antialias = bool
        text_colour = namedtuple('colour', ['r', 'g', 'b'])

        Nothing is returned
        '''

        # Screen variables
        self.screen = screen
        self.position = position

        # Text variables
        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)
        self.font = pygame.font.Font(font_family, font_size)
        self.font_size = font_size
        self.antialias = antialias
        self.value = value
        self.text_colour = text_colour

        # Create Textbox objects
        self.create()

    def create(self) -> None:
        '''
        creates Textbox, text, and cursor objects.

        Nothing is returned
        '''

        # Text
        self.value_object = self.font.render(self.value, self.antialias,
                                      self.text_colour)

    def update(self) -> None:
        '''
        Redraws label value

        Nothing is returned
        '''

        self.screen.blit(self.value_object, self.position)
        
