import pygame

BLACK = (0,0,0)

class Spritesheet:
    def __init__(self, image) -> None:
        self.sheet = image

    def get_sprite(self, frame, width, height, scale): #scale optional if want to resize
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0,0), ((frame * width), 0, width, height)) #source, where it starts on the blit, starting coords, ending coords
        sprite = pygame.transform.scale(sprite, (width * scale, height * scale))
        sprite.set_colorkey(BLACK)
        return sprite