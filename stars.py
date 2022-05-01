import pygame

class Star():
    def __init__(self, colorID, coords):
        
        if colorID == None:
            self.colorID = 0
        else:
            self.colorID = colorID  # color ID.

        self.coords = coords  # coords position of screen.
        self.color = (255, 0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.coords)
