'''
David Fuller

Textbox class for forms in Pygame

2017-11-21
'''

import pygame
import os.path

from .Constants import point, color

pygame.font.init()

class textbox_event(object):
    '''
    Mocks an enumerable for textbox events
    '''
    
    nothing = 0
    enter = 1
    click = 2
    tab = 3
    

class Textbox(object):
    '''
    Textbox class for forms in Pygame. The value of the textbox can be
    retrieved using object.value.
    '''

    def __init__(self,
                 position = point(x = 0, y = 0),
                 character_count = 50,
                 font_family = 'Helvetica',
                 font_size = 20,
                 antialias = True,
                 text_color = color(r = 0, g = 0, b = 0),
                 box_color = color(r = 0, g = 0, b = 0),
                 background_color = color(r = 127, g = 127, b = 127),
                 border_width = 2):
        '''
        init for Textbox class.
        
        Args:
            position (namedtuple('point', ['x', 'y'])): position of textbox
            character_count (int): total number of characters allowed in textbox
            font_family (ttf): font family of text in textbox
            font_size (int): size of font for text in textbox
            antialias (bool): whether or not text is antialiased
            text_color (namedtuple('color', ['r', 'g', 'b'])): color of text
                                                                 in textbox
            box_color (namedtuple('color', ['r', 'g', 'b'])): color of textbox
                                                                border
            background_color (namedtuple('color', ['r', 'g', 'b'])): color of
                                                                     textbox
                                                                     background
            border_width (int): pixels wide for border of textbox
        '''

        # Screen variables
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
        self.text_color = text_color
        self.box_color = box_color
        self.background_color = background_color
        self.border_width = border_width
        self.text_align = 'left'
        self.bold = False

        # Create Textbox objects
        self.create()

    def create(self):
        '''
        Creates Textbox and text objects.
        '''

        # Textbox
        self.text_width, self.text_height = self.font.size('M')
        self.box_dimension = point(x = self.text_width * self.character_count,
                                   y = self.text_height + self.border_width * 2)
        self.box = pygame.Rect(self.position, self.box_dimension)

        # Decorate text
        self.align()
        self.set_bold()

        # Set texxt object
        self.value_object = self.font.render(self.value, self.antialias,
                                             self.text_color)
        
    def set_bold(self):
        '''
        Sets whether Cell text is bold or not.
        '''

        self.font.set_bold(self.bold)
        self.align()

        # Set texxt object
        self.value_object = self.font.render(self.value, self.antialias,
                                             self.text_color)

    def align(self):
        '''
        Aligns text in Textbox.
        '''
        
        text_width, text_height = self.font.size(self.value)
        if self.text_align == 'left':
            text_x = self.position.x + self.border_width * 2
        elif self.text_align == 'center':
            text_x = int((self.box_dimension.x - text_width) / 2) + self.position.x
        text_y = int((self.box_dimension.y - text_height) / 2) + self.position.y
        self.text_position = point(x = text_x, y = text_y)

    def change_value(self, value):
        '''
        Changes value of textbox.

        Args:
            value (str): string value of the textbox
        '''

        self.value = value

        # Make text fit box
        x, y = self.font.size(self.value)
        overall_width = x
        while overall_width > self.box_dimension.x - (self.border_width * 2):
            self.value = self.value[:len(self.value) - 1]
            x, y = self.font.size(self.value)
            overall_width = x

        # Decorate text
        self.align()
        self.set_bold()

        # Set text object
        self.value_object = self.font.render(self.value, self.antialias,
                                             self.text_color) 

    def show(self, surface):
        '''
        Show textbox elements on screen.

        Args:
            surface (pygame surface): surface to draw on
        '''
        
        # Display Textbox
        pygame.draw.rect(surface, self.background_color,
                         self.box)
        pygame.draw.rect(surface, self.box_color,
                         self.box, self.border_width)

        # Display text
        surface.blit(self.value_object, self.text_position)        

class InputBox(Textbox):
    '''
    InputBox class for forms in Pygame. Can be used for input or password.
    Setting is_password to True makes it a password input, where text is
    masked. The value of the textbox can be retrieved using object.value.
    '''
    
    def __init__(self,
                 position = point(x = 0, y = 0),
                 character_count = 50,
                 font_family = 'Helvetica',
                 font_size = 20,
                 antialias = True,
                 text_color = color(r = 0, g = 0, b = 0),
                 box_color = color(r = 0, g = 0, b = 0),
                 background_color = color(r = 127, g = 127, b = 127),
                 border_width = 2,
                 is_password = False,
                 tab_index = 0):
        '''
        init for InputBox class.
        
        Args:
            position (namedtuple('point', ['x', 'y'])): position of InputBox
            character_count (int): total number of characters allowed in InputBox
            font_family (ttf): font family of text in InputBox
            font_size (int): size of font for text in InputBox
            antialias (bool): whether or not text is antialiased
            text_color (namedtuple('color', ['r', 'g', 'b'])): color of text
                                                                 in InputBox
            box_color (namedtuple('color', ['r', 'g', 'b'])): color of InputBox
                                                                border
            background_color (namedtuple('color', ['r', 'g', 'b'])): color of
                                                                     InputBox
                                                                     background
            border_width (int): pixels wide for border of InputBox
            is_password (bool): whether or not text is masked
        '''
        
        Textbox.__init__(self, position, character_count, font_family, font_size,
                         antialias, text_color, box_color, backgroun_color,
                         border_width)

        self.is_password = is_password
        self.password = ''
        self.tab_index = tab_index

        self.active = False
        if self.tab_index == 0:
            self.active = True
        
         # Cursor variables
        self.cursor_visible = True
        self.blink_seconds = 0.25
        self.frame_count = 0
        self.cursor_index = 0
        self.cursor_position = None

        self.create()

    def create(self):
        '''
        Creates InputBox objects.
        '''
        
        Textbox.create(self)
        
        # Cursor
        self.cursor_position = point(x = self.text_position.x - int(self.border_width / 2),
                                     y = int((self.box_dimension.y - self.text_height) / 2) + self.position.y)
        self.cursor_dimension = point(x = 2,
                                      y = self.text_height)
        self.cursor = pygame.Rect(self.cursor_position, self.cursor_dimension)

    def clicked(self):
        '''
        Decides whether or not textbox was clicked.

        Returns:
            True: textbox was clicked
            False: textbox was not clicked
        '''
        
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseX > self.position.x and \
           mouseX < self.position.x + self.box_dimension.x and \
           mouseY > self.position.y and \
           mouseY < self.position.y + self.box_dimension.y:
            return True
        return False

    def update(self, events, fps):
        '''
        Updates Texbox attributes and displays text, box, background, and
        cursor appropriately.

        Args:
            events (pygame.events): mouse click, keyboard key press
            fps (int): applicaiton's frames per second

        Returns:
           textbox_event.nothing: 0 for nothing happening
           textbox_event.enter: 1 if enter or return are hit
           textbox_event.click: 2 if textbox is clicked
        '''

        # Handle key presses
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.clicked() == True:
                    return textbox_event.click
                
            if event.type == pygame.KEYDOWN and \
               event.key != pygame.K_RSHIFT and \
               event.key != pygame.K_LSHIFT:

                if event.key == pygame.K_BACKSPACE:
                    if self.is_password:
                        self.password = self.password[:max(self.cursor_index - 1, 0)] + \
                                        self.password[self.cursor_index:]
                        self.value = ''
                        for i in range(len(self.password)):
                            self.value = self.value + '*'
                    else:
                        self.value = self.value[:max(self.cursor_index - 1, 0)] + \
                                        self.value[self.cursor_index:]
                    self.value_object = self.font.render(self.value, self.antialias,
                                                         self.text_color)
                    self.cursor_index = max(self.cursor_index - 1, 0)

                elif event.key == pygame.K_DELETE:
                    if self.is_password:
                        self.password = self.password[:self.cursor_index] + \
                                        self.password[self.cursor_index + 1:]
                        self.value = ''
                        for i in range(len(self.password)):
                            self.value = self.value + '*'
                    else:
                        self.value = self.value[:self.cursor_index] + \
                                        self.value[self.cursor_index + 1:]
                    self.value_object = self.font.render(self.value, self.antialias,
                                          self.text_color)

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
                    return textbox_event.enter

                elif event.key == pygame.K_TAB:
                    self.active = False
                    return textbox_event.tab

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
                     event.key == pygame.K_INSERT or \
                     event.key == pygame.K_PAGEUP or \
                     event.key == pygame.K_PAGEDOWN or \
                     event.key == pygame.K_ESCAPE or \
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
                    if self.active:
                        overall_width = 0
                        for i in range(self.cursor_index):
                            x, y = self.font.size(self.value[i])
                            overall_width += x
                        width, height = self.font.size(event.unicode)
                        if overall_width + width < self.box_dimension.x - (self.border_width * 2):
                            try:
                                if self.is_password:
                                    self.password = self.password[:self.cursor_index] + \
                                                    event.unicode + \
                                                    self.password[self.cursor_index:]
                                    self.value = ''
                                    for i in range(len(self.password)):
                                        self.value = self.value + '*'
                                else:
                                    self.value = self.value[:self.cursor_index] + \
                                                    event.unicode + \
                                                    self.value[self.cursor_index:]
                                self.value_object = self.font.render(self.value, self.antialias,
                                                                     self.text_color)
                                self.cursor_index = self.cursor_index + 1
                            except:
                                pass

        # Handle cursor visibility
        if self.active:
            self.frame_count = self.frame_count + 1
            if self.frame_count >= self.blink_seconds * fps:
                self.cursor_visible = not self.cursor_visible
                self.frame_count = 0
                
            cursor_x = self.text_position.x - int(self.border_width / 2)
            space_count = 0
            for i in range(self.cursor_index):
                x, y = self.font.size(self.value[i])
                cursor_x = cursor_x + x
            self.cursor_position = self.cursor_position._replace(x = cursor_x)
            self.cursor = pygame.Rect(self.cursor_position, self.cursor_dimension)
            
        return textbox_event.nothing         

    def show(self, surface):
        '''
        Show InputBox elements on screen.

        Args:
            surface (pygame surface): surface to draw on
        '''
        
        Textbox.show(self, surface)
        
        # Display cursor
        if self.active:
            if (self.cursor_visible == True):
                pygame.draw.rect(surface, self.text_color, self.cursor)
