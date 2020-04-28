import pygame

class Button():
    def __init__(self,
        x, y, w, h,

        text='',
        text_size=30,
        font='ariel',

        main_color=(255, 255, 255),
        text_colour=(0, 0, 0),
        hover_colour=(200, 200, 200),
        pressed_colour=(200, 100, 100),

        surface_to_draw_to=None,
        ):
        """
        Button class
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)

        self.text = text
        self.text_size = text_size
        self.font = font

        self.main_color = main_color
        self.text_colour = text_colour
        self.hover_colour = hover_colour
        self.pressed_colour = pressed_colour

        self.screen = surface_to_draw_to

        self.hover = False
        self.pressed = False

    def create_text(self, surface):
        # create and draw text
        font = pygame.font.SysFont(self.font, self.text_size)
        label = font.render(self.text, True, self.text_colour)

        lbl_w, lbl_h = label.get_size()
        x_offset = (self.w / 2) - lbl_w / 2
        y_offset = (self.h / 2) - lbl_h / 2
        surface.blit(label, (self.x + x_offset, self.y + y_offset))

    def create_rect(self, surface):
        # update rect and draw button
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        if self.hover : color = self.hover_colour
        else : color = self.main_color
        if self.pressed : color = self.pressed_colour

        pygame.draw.rect(surface, color, self.rect)

    def update(self, mouse_pos, mouse_press, button_to_be_activated_by=(1, 0, 0)):
        """
        Updates button colours based on mouse states
        returns a boolean based on wheather the button has been pressed or not
        """
        mx, my = mouse_pos
        self.hover = self.rect.collidepoint(mx, my)

        if self.hover and mouse_press == (1, 0, 0):
            self.pressed = True
            return True
        else:
            self.pressed = False
            return False

    def show(self, *args):
        """
        Draws the button to a surface
        if the surface has been set upon initialisation of this object, no surface argument is required
        otherwise a surface argument is required
        """
        if self.screen is not None:
            surface = self.screen
        elif len(args) == 0 and self.screen is None:
            raise ValueError('Please pass in a surface to draw to')
        elif len(args) == 1:
            surface = args[0]

        self.create_rect(surface)
        self.create_text(surface)



