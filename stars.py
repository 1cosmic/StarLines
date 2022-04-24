import pygame

class Star():
    def __init__(self, colorID, coords):
        self.colorID = colorID  # color ID.
        self.coords = coords  # coords position of screen.
        self.color = (255, 0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, color, self.coords)
