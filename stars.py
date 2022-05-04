import pygame

class Star():
    def __init__(self, colorID, coords):

        self.colorID = colorID  # color ID.
        
        self.coord_X = coords[0]  # coords position of screen.
        self.coord_Y = coords[1]  # coords position of screen.

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
        __rect = self.coord_X, self.coord_Y, 60, 60
        pygame.draw.rect(screen, self.color, __rect)