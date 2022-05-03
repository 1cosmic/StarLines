import random
import pygame
import os

from field import Field


class CLines():

    def __init__(self):
        pygame.init()  # initialize of library.

        # Settings of the APP.
        self.win_size = width, height = 1200, 750
        self.win_bgrd = pygame.image.load(os.path.join("Materials", "background-1200x750.jpg"))

        self.mainScreen = pygame.display.set_mode(self.win_size)  # create main window.

        self.start_pos = ((800 - (9 * 50) / 2), (600 - (9 * 50) / 2))

        self.field = Field(self.mainScreen, self.win_size)

    def run(self):
        run = True
        self.mainScreen.blit(self.win_bgrd, (0, 0))  # fill background.
        self.field.draw(self.win_size)

        color_list = [self.randomColor for i in range(3)]  # create colors list.

        while run:
            # Main cycle of APP.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        self.field.crtRandomStar()

            pygame.display.flip()  # last frame.
            pygame.time.delay(100)  # lock of the speed.

        else:
            print("Game was close")

    @staticmethod
    def randomColor(colorList):
        """Generate list with 3-e random colors."""
        return [random.randint(1, 7) * 3]
