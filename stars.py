import pygame

class Star():
    def __init__(self, colorID, coords):
        
        if colorID == None:
            self.colorID = 0
        else:
            self.colorID = colorID  # color ID.

        self.coords = coords  # coords position of screen.
        if colorID == 1: 
            self.color = (255, 0, 0)      # red.
        elif colorID == 2: 
            self.color = (255, 200, 0)     # orange.
        elif colorID == 3: 
            self.color = (255, 255, 0)     # yellow.
        elif colorID == 4: 
            self.color = (0, 255, 0)       # green.
        elif colorID == 5: 
            self.color = (0, 255, 255)     # light-blue.
        elif colorID == 6: 
            self.color = (0, 0, 255)       # blue.
        elif colorID == 7: 
            self.color = (255, 0, 255)     # puple.

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.coords)
