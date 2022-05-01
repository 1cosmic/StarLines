import random
import pygame

from stars import Star

class Field():
    def __init__(self, screen):
        self.screen = screen
        
        # Create matrix of star-object.
        self.matrix = [[0] * 9 for i in range(9)]

        # And inizialize it!
        for y in range(9):
            for x in range(9):
                self.createStar(y, x)
        
        # For check of free cell in matrix.
        self.free_matrix = [[i] * 9 for i in range(9)]


    def draw_star_block(self, pos_x, pos_y):
        """Draw star background."""

        # Background
        bg = (0, 0, 0)

        # Set property & position.
        pos_x += self.space
        pos_y += self.space
        __block_pos = (pos_x, pos_y, self.block_w, self.block_w)

        # Display block with margin.
        pygame.draw.rect(self.screen, bg, __block_pos)


    def draw_line(self, start_x, start_y):
        """Draw line, who separate to stars."""

        start_x += 2  # set up currect coorditates of first line (bug fix).

        _color = (255, 255, 255)
        _speed = 10

        __line_V = [[start_x, start_y], [start_x, start_y]]
        __line_H = [[start_x, start_y], [start_x, start_y]]

        while __line_V[1][1] - __line_V[0][1] < self.line_l:

            __line_V[0][0] = start_x
            __line_H[0][1] = start_y

            for i in range(8):
                __line_V[0][0] += self.block_margin
                __line_V[1][0] = __line_V[0][0]

                pygame.draw.line(self.screen, _color, __line_V[0], __line_V[1], self.line_w)

                __line_H[0][1] += self.block_margin
                __line_H[1][1] = __line_H[0][1]


                # pygame.display.update()
                pygame.draw.line(self.screen, _color, __line_H[0], __line_H[1], self.line_w)

            __line_H[1][0] += _speed
            __line_V[1][1] += _speed
            pygame.time.delay(10)
            pygame.display.update()


    def draw_star(self):
        pass

    def draw(self, win_size):
        """Draw field in surface."""

        self.block_w = 60
        self.line_w = 2
        self.space = 6

        self.block_margin = self.block_w + self.space
        self.line_l = self.block_margin * 9

        pos_x = (win_size[0] - self.line_l) / 2
        pos_y = (win_size[1] - self.line_l) / 2  # set up start position.
        
        self.startXY = pos_x, pos_y  # сохраняем стартовые координаты.

        # Draw separate line.
        self.draw_line(pos_x, pos_y)

        # Draw is step-to-step for stars on screen.
        for line in self.matrix:

            # Draw block.
            self.draw_star_block(pos_x, pos_y)


            # Animated draw.
            pygame.time.delay(10)
            pygame.display.update()


    def startPosStar(self, ID_X, ID_Y):
        """Получить стартовые координаты звезды."""
        X = self.startXY[0]
        Y = self.startXY[1] 
       
        for i_x in range(ID_X): 
            X += self.block_margin
            for i_y in range(ID_Y):
                Y += self.block_margin

        return X, Y


    def createStar(self, colorID, coord_XY):
        """Добавляет объект звезды в поле."""
        X = coord_XY[0]
        Y = coord_XY[1]

        return Star(colorID, self.startPosStar(X, Y))


    def randomFreeCell(self):
        """Return x & y of free cell in matrix."""
        
        # Create randomize list of string.
        randomStr = random.sample(self.free_matrix, len(self.free_matrix))
        # If string non free, lets go to next str!
        for string in randomStr:
            if len(string) != 0:

                cell = random.choice(string)
                string.remove(cell)
                string = self.free_matrix.index(string)  # re-write value.


    def crtRandomStar(self, count):
        """Place random Star in random cell x-count."""

        for i in count:
            pass
