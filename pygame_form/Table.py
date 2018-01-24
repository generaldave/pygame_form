'''
David Fuller

Table class for forms in Pygame

2018-1-18
'''

import pygame
import os.path

from .Constants import point, color
from .Textbox import Textbox

pygame.font.init()

class Table(object):
    '''
    Table class for forms in Pygame. Values can be retrieved using cells array
    '''

    def __init__(self,
                 position = point(x = 0, y = 0),
                 row_count = 3,
                 column_count = 3,
                 has_header = False,
                 font_family = 'Helvetica',
                 font_size = 20,
                 antialias = True,
                 text_align = 'left',
                 text_color = color(r = 0, g = 0, b = 0),
                 box_color = color(r = 0, g = 0, b = 0),
                 background_color = color(r = 127, g = 127, b = 127),
                 border_width = 2):
        '''
        init for Table class.
        
        Args:
            position (namedtuple('point', ['x', 'y'])): position of textbox
            row_count (int): total number of rows in table
            column_count (int): total number of columns in table
            has_header (bool): wether or not there is a header row
            font_family (ttf): font family of text in textbox
            font_size (int): size of font for text in textbox
            antialias (bool): whether or not text is antialiased
            text_color (namedtuple('color', ['r', 'g', 'b'])): color of text
                                                                 in Table
            box_color (namedtuple('color', ['r', 'g', 'b'])): color of Table
                                                                border
            background_color (namedtuple('color', ['r', 'g', 'b'])): color of
                                                                     Cell
                                                                     background
            border_width (int): pixels wide for border of textbox
        '''

        # Screen variables
        self.position = position

        # Table variables
        self.row_count = row_count
        self.column_count = column_count
        self.has_header = has_header
        self.text_align = text_align
        self.text_color = text_color
        self.box_color = box_color
        self.background_color = background_color
        self.border_width = border_width

        # Text variables
        self.font_family = font_family
        self.font_size = font_size
        self.antialias = antialias
        self.cells = []   

        # Create Table objects
        self.create()

    def create(self):
        '''
        Creates Table and Cell objects.
        '''

        self.cells = []

        hue_1 = 127
        hue_2 = 63
        hue = hue_1
        blue = 200
        x = self.position.x
        y = self.position.y

        if self.has_header:
            bold = True
        else:
            bold = False
            
        for row in range(self.row_count):
            for column in range(self.column_count):
                cell = Textbox(position = point(x = x, y = y),
                               character_count = 10,
                               font_family = self.font_family,
                               font_size = self.font_size,
                               antialias = self.antialias,
                               text_color = self.text_color,
                               box_color = color(r = hue, g = hue, b = blue),
                               background_color = color(r = hue, g = hue, b = blue),
                               border_width = 0)
                cell.bold = bold
                cell.text_align = self.text_align
                self.cells.append(cell)
                cell.change_value('test text')
                x = x + (cell.text_width * cell.character_count) + 2
            bold = False
            hue = hue_2 if hue == hue_1 else hue_1
            x = self.position.x
            y = y + cell.text_height + 2

    def center(self, surface_resolution):
        '''
        Center table to a given surface.

        Args:
            surface_resolion (point): width and height of surface to center to.
        '''
        
        cell_width = self.cells[0].text_width
        table_width = ((cell_width * self.cells[0].character_count) * self.column_count) + \
                      2 * (self.column_count - 1)
        table_x = int((surface_resolution.width / 2) - (table_width / 2))

        self.position = point(x = table_x, y = self.position.y)

        self.create()

    def show(self, surface):
        '''
        Shows the table on a given surface.

        Args:
            surface (pygame.surface): Surface to show table on.
        '''
        
        for cell in self.cells:
            cell.show(surface)


        

