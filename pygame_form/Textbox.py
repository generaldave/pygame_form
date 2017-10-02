'''
David Fuller

Textbox class for forms in Pygame

2017-9-30
'''

import pygame
import os.path

from collections import namedtuple

point = namedtuple('point', ['x', 'y'])
colour = namedtuple('colour', ['r', 'g', 'b'])
pygame.font.init()

class Textbox(object):
    '''
    Textbox class for forms in Pygame. Can be used for input or output.
    Setting input_box to True makes it an input box. If set as input, a cursor
    exists. Otherwise, it does not. The value of the textbox can be retrieved
    using object.value.
    '''

    def __init__(self, screen,
                 position = point(x = 0, y = 0),
                 character_count = 50,
                 font_family = 'Helvetica',
                 font_size = 20,
                 antialias = True,
                 text_colour = colour(r = 0, g = 0, b = 0),
                 box_colour = colour(r = 0, g = 0, b = 0),
                 border_width = 2,
                 input_box = False) -> None:
        '''
        init for Textbox class.

        screen = pygame.display
        position = namedtuple('point', ['x', 'y'])
        character_count = int
        font_family = ttf
        font_size = int
        antialias = bool
        text_colour = namedtuple('colour', ['r', 'g', 'b'])
        box_colour = namedtuple('colour', ['r', 'g', 'b'])
        border_width = int
        input_box = bool

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
        self.value_object = None
        self.value = ''

        # Textbox variables
        self.text_colour = text_colour
        self.box_colour = box_colour
        self.border_width = border_width

        # Texbox type: input or not
        self.input_box = input_box

        # Cursor variables
        self.cursor_visible = True
        self.blink_seconds = 0.25
        self.frame_count = 0
        self.cursor_index = 0
        self.cursor_position = None

        # Create Textbox objects
        self.create()

    def create(self) -> None:
        '''
        creates Textbox, text, and cursor objects.

        Nothing is returned
        '''

        # Textbox
        self.text_width, self.text_height = self.font.size('M')
        self.box_dimension = point(x = self.text_width * self.character_count,
                                   y = self.text_height + self.border_width * 2)
        self.box = pygame.Rect(self.position, self.box_dimension)

        # Text
        self.value_object = self.font.render(self.value, self.antialias,
                                             self.text_colour)
        text_x = self.position.x + self.border_width * 2
        text_y = int((self.box_dimension.y - self.text_height) / 2) + self.position.y
        self.text_position = point(x = text_x, y = text_y)

        # Cursor
        self.cursor_position = point(x = self.text_position.x - int(self.border_width / 2),
                                     y = int((self.box_dimension.y - self.text_height) / 2) + self.position.y)
        self.cursor_dimension = point(x = 2,
                                      y = self.text_height)
        self.cursor = pygame.Rect(self.cursor_position, self.cursor_dimension)

    def update(self, events, fps) -> None:
        '''
        updates Texbox attributes and displays text, box, background, and
        cursor appropriately.

        events = pygame.events
        fps = int

        Nothing is returned
        '''

        # Handle key presses
        for event in events:
            if event.type == pygame.KEYDOWN and \
               event.key != pygame.K_RSHIFT and \
               event.key != pygame.K_LSHIFT and \
               self.input_box == True:

                if event.key == pygame.K_BACKSPACE:
                    self.value = self.value[:max(self.cursor_index - 1, 0)] + \
                                        self.value[self.cursor_index:]
                    self.value_object = self.font.render(self.value, self.antialias,
                                                         self.text_colour)
                    self.cursor_index = max(self.cursor_index - 1, 0)

                elif event.key == pygame.K_DELETE:
                    self.value = self.value[:self.cursor_index] + \
                                        self.value[self.cursor_index + 1:]
                    self.value_object = self.font.render(self.value, self.antialias,
                                          self.text_colour)

                elif event.key == pygame.K_LEFT:
                    self.cursor_index = max(self.cursor_index - 1, 0)

                elif event.key == pygame.K_RIGHT:
                    self.cursor_index = min(self.cursor_index + 1, len(self.value))
                    
                elif event.key == pygame.K_END:
                    self.cursor_index = len(self.value)

                elif event.key == pygame.K_HOME:
                    self.cursor_index = 0

                elif event.key == pygame.K_RETURN or \
                     event.key == pygame.K_KP_ENTER:
                    print ("hit enter")

                elif event.key == pygame.K_UP or \
                     event.key == pygame.K_DOWN or \
                     event.key == pygame.K_CAPSLOCK or \
                     event.key == pygame.K_NUMLOCK or \
                     event.key == pygame.K_SCROLLOCK or \
                     event.key == pygame.K_LCTRL or \
                     event.key == pygame.K_RCTRL or \
                     event.key == pygame.K_LALT or \
                     event.key == pygame.K_RALT or \
                     event.key == pygame.K_LSUPER or \
                     event.key == pygame.K_RSUPER or \
                     event.key == pygame.K_PRINT or \
                     event.key == pygame.K_MODE or \
                     event.key == pygame.K_HELP or \
                     event.key == pygame.K_LMETA or \
                     event.key == pygame.K_RMETA or \
                     event.key == pygame.K_SYSREQ or \
                     event.key == pygame.K_BREAK or \
                     event.key == pygame.K_MENU or \
                     event.key == pygame.K_POWER or \
                     event.key == pygame.K_EURO or \
                     event.key == pygame.K_TAB or \
                     event.key == pygame.K_INSERT or \
                     event.key == pygame.K_PAGEUP or \
                     event.key == pygame.K_PAGEDOWN or \
                     event.key == pygame.K_F1 or \
                     event.key == pygame.K_F2 or \
                     event.key == pygame.K_F3 or \
                     event.key == pygame.K_F4 or \
                     event.key == pygame.K_F5 or \
                     event.key == pygame.K_F6 or \
                     event.key == pygame.K_F7 or \
                     event.key == pygame.K_F8 or \
                     event.key == pygame.K_F9 or \
                     event.key == pygame.K_F10 or \
                     event.key == pygame.K_F11 or \
                     event.key == pygame.K_F12 or \
                     event.key == pygame.K_F13 or \
                     event.key == pygame.K_F14 or \
                     event.key == pygame.K_F15:
                    pass

                else:
                    overall_width = 0
                    for i in range(self.cursor_index):
                        x, y = self.font.size(self.value[i])
                        overall_width += x
                    width, height = self.font.size(event.unicode)
                    if overall_width + width < self.box_dimension.x - (self.border_width * 2):
                        try:
                            self.value = self.value[:self.cursor_index] + \
                                                event.unicode + \
                                                self.value[self.cursor_index:]
                            self.value_object = self.font.render(self.value, self.antialias,
                                                                 self.text_colour)
                            self.cursor_index = self.cursor_index + 1
                        except:
                            pass
                    
                cursor_x = self.text_position.x - int(self.border_width / 2)
                space_count = 0
                for i in range(self.cursor_index):
                    x, y = self.font.size(self.value[i])
                    cursor_x = cursor_x + x
                self.cursor_position = self.cursor_position._replace(x = cursor_x)
                self.cursor = pygame.Rect(self.cursor_position, self.cursor_dimension)
                
        # Display Textbox
        pygame.draw.rect(self.screen, self.box_colour,
                         self.box, self.border_width)

        # Display text
        self.screen.blit(self.value_object, self.text_position)

        # Display cursor
        if (self.cursor_visible == True and self.input_box == True):
            pygame.draw.rect(self.screen, self.text_colour, self.cursor)

        # Handle cursor visibility
        if self.input_box == True:
            self.frame_count = self.frame_count + 1
            if self.frame_count >= self.blink_seconds * fps:
                self.cursor_visible = not self.cursor_visible
                self.frame_count = 0
