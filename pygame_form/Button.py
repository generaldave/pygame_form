'''
David Fuller

Button class for forms in Pygame

2017-10-1
'''

import pygame
import os.path

from collections import namedtuple

point = namedtuple('point', ['x', 'y'])
colour = namedtuple('colour', ['r', 'g', 'b'])
pygame.font.init()

class Button(object):
    '''
    Button class for forms in Pygame.
    '''
    
    def __init__(self, screen,
                 position = point(x = 0, y = 0),
                 value = 'Acccept',
                 character_count = 5,
                 font_family = 'Helvetica',
                 font_size = 20,
                 antialias = True,
                 text_colour = colour(r = 0, g = 0, b = 0),
                 box_colour = colour(r = 0, g = 0, b = 0)) -> None:
        '''
        init for Button class.

        screen = pygame.display
        position = namedtuple('point', ['x', 'y'])
        value = str
        character_count = int
        font_family = ttf
        font_size = int
        antialias = bool
        text_colour = namedtuple('colour', ['r', 'g', 'b'])
        box_colour = namedtuple('colour', ['r', 'g', 'b'])

        Nothing is returned
        '''

        # Screen variables
        self.screen = screen
        self.position = position

        # Text variables
        self.character_count = character_count
        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)
        self.font = pygame.font.Font(font_family, font_size)
        self.font_size = font_size
        self.antialias = antialias
        self.value = value
        self.value_object = None

        # Button variables
        self.text_colour = text_colour
        self.box_colour = box_colour

        # Create Button objects
        self.create()

    def create(self) -> None:
        '''
        Creates button and value objects

        Nothing is returned
        '''
        
        # Box
        self.text_width, self.text_height = self.font.size('M')
        self.box_dimension = point(x = self.text_width * self.character_count,
                                   y = self.text_height)
        self.box = pygame.Rect(self.position, self.box_dimension)

        # Value
        self.value_object = self.font.render(self.value, self.antialias,
                                             self.text_colour)
        width, height = self.font.size(self.value)
        text_x = int((self.box_dimension.x - width) / 2) + self.position.x
        text_y = int((self.box_dimension.y - self.text_height) / 2) + self.position.y
        self.text_position = point(x = text_x, y = text_y)

    def clicked(self, mouseX, mouseY) -> bool:
        '''
        Decides whether or not button has been clicked. Returns True if yes
        and False if not.
        '''

        if mouseX > self.position.x and \
           mouseX < self.position.x + self.box_dimension.x and \
           mouseY > self.position.y and \
           mouseY < self.position.y + self.box_dimension.y:
            return True

        return False

    def update(self) -> None:
        '''
        Displays button and value objects

        Nothing is returned
        '''
        
        # Display Button
        pygame.draw.rect(self.screen, self.box_colour, self.box)
        self.screen.blit(self.value_object, self.text_position)
