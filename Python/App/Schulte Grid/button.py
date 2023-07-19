import pygame

class Text():
    def __init__(self, x, y, f_size):
        self.x, self.y =x, y
        self.font = pygame.font.SysFont(None, int(f_size))

    def form_text(self, te_color, text):
        self.text = text
        self.text_image = self.font.render(text, True, te_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.x = self.x
        self.text_image_rect.y = self.y

    def draw(self, screen):
        screen.blit(self.text_image, self.text_image_rect)



class Button():
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(None, int(0.75*self.rect.h))

    def form_text(self, te_color, text):
        self.text = text
        self.text_image = self.font.render(self.text, True, te_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw(self, screen, bu_color, edge = None):
        if edge:
            thickness = int(0.06 * self.rect.h)
            pygame.draw.rect(screen, bu_color, self.rect, thickness)
        else:
            pygame.draw.rect(screen, bu_color, self.rect)
        
        screen.blit(self.text_image, self.text_image_rect)




class InputBox(Button):
    def __init__(self, x, y, width, height, l_max):
        super().__init__(x, y, width, height)
        self.active = False
        self.max = l_max

    def add_letter(self, te_color, letter):
        if len(self.text) < self.max:
            self.text = self.text + letter
        self.text_image = self.font.render(self.text, True, te_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def cancel_letter(self, te_color, letter):
        self.text = self.text[:-1]
        self.text_image = self.font.render(self.text, True, te_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw(self,  screen, bu_color, bu_active_color):
        thickness = int(0.064 * self.rect.h)
        if self.active:
            pygame.draw.rect(screen, bu_active_color, self.rect, thickness)
        else:
            pygame.draw.rect(screen, bu_color, self.rect, thickness)
        
        screen.blit(self.text_image, self.text_image_rect)
        






