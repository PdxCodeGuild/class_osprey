import pygame

pygame.init()

FONT = pygame.font.SysFont('Courier', 17)
WHITE = (255, 255, 255)


class Button():
    def __init__(self, base, hover, press, x, y) -> None:
        self.base = base
        base = pygame.image.load(base)
        hover = pygame.image.load(hover)
        press = pygame.image.load(press)
        self.base = pygame.transform.scale(base, (base.get_width()*2 , base.get_height()*2))
        self.hover = pygame.transform.scale(hover, (hover.get_width()*2 , hover.get_height()*2))
        self.press = pygame.transform.scale(press, (press.get_width()*2 , press.get_height()*2))
        self.rect = self.base.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def display(self, screen, hovertext='', x=0, y=0):
        hoverphrase = FONT.render(hovertext, False, WHITE)
        button_action = False
        screen.blit(self.base, (self.rect.topleft))
        mouse_pos = pygame.mouse.get_pos()
        #look for mouseover
        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.hover, (self.rect.topleft))
            screen.blit(hoverphrase, (x, y))
            if pygame.mouse.get_pressed()[0] == True and not self.clicked: 
            #0 index is LMB, pressed looks for T/F 1/0
                screen.blit(self.press, (self.rect.topleft))
                self.clicked = True
                button_action = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
        return button_action