import random
import pygame

from stars import Star


class Field():
    def __init__(self, screen, win_size):
        self.screen = screen

        self.block_w = 60
        self.line_w = 2
        self.space = 6

        self.block_margin = self.block_w + self.space
        self.line_l = self.block_margin * 9

        pos_x = 2 + (win_size[0] - self.line_l) / 2
        pos_y = 2 + (win_size[1] - self.line_l) / 2  # set up start position.

        self.startXY = (pos_x, pos_y)  # сохраняем стартовые координаты.

        # Create matrix of star-object.
        self.matrix = [[0] * 9 for i in range(9)]

        # And inizialize it!
        for y in range(9):
            for x in range(9):
                self.matrix[y][x] = Star(0, self.startPosStar(x, y))

        # For check of free cell in matrix.
        self.free_matrix = [[i for i in range(9)] for i2 in range(9)]

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

    def draw_line(self):
        """Draw line, who separate to stars."""
        start_x = self.startXY[0]
        start_y = self.startXY[1]

        # start_x += 2  # set up currect coorditates of first line (bug fix).

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

        # Draw separate line.
        self.draw_line()

        # Draw is step-to-step for stars on screen.
        # for line in self.matrix:

        # Draw block.

        # Animated draw.
        # pygame.time.delay(10)
        # pygame.display.update()

    def startPosStar(self, ID_X, ID_Y):
        """Получить стартовые координаты звезды."""
        X = self.startXY[0] + 4
        Y = self.startXY[1] + 4

        for i_x in range(ID_X):
            X += self.block_margin
        for i_y in range(ID_Y):
            Y += self.block_margin

        return X, Y

    def randomFreeCell(self):
        """Return x & y of free cell in matrix."""

        # Create randomize list of string.
        run = True
        while run:  # while we don`t find free cell:
            randomStrID = random.randint(0, 8)  # random string ID.
            randomStr = self.free_matrix[randomStrID]  # save this string.

            if len(randomStr):  # if there is free cell:
                randomCell = random.choice(randomStr)
                self.free_matrix[randomStrID].remove(randomCell)  # fill cell.

                # print("Рандомная ячейка: ", randomStrID, randomCell)
                return randomStrID, randomCell

    def crtRandomStar(self):
        """Добавляет объект звезды в поле."""
        colorID = random.randint(1, 7)
        randomXY = self.randomFreeCell()
        X = randomXY[0]
        Y = randomXY[1]

        self.matrix[X][Y] = Star(colorID, self.startPosStar(X, Y))
        self.matrix[X][Y].draw(self.screen)

        print("Создана звезда.")

    def fullCheckLines(self):
        check = True
        for x in range(9):
            STR_counter = 0
            CLMN_counter = 0

            STR_last_color = None
            CLMN_last_color = None

            STR_start = 0
            CLMN_start = 0

            for y in range(9):

                STR_cur = self.matrix[x][y].colorID
                if STR_cur != 0:
                    STR_last_color = STR_cur
                    if STR_last_color == self.matrix[x][y]:
                        STR_counter += 1
                        print(STR_counter)
                        if STR_start == 0:
                            STR_start = y
                else:
                    STR_counter = 0
                    STR_start = 0

                CLMN_cur = self.matrix[y][x].colorID
                if CLMN_cur != 0:
                    CLMN_last_color = CLMN_cur
                    if CLMN_last_color == self.matrix[y][x]:
                        CLMN_counter += 1
                        if CLMN_start == 0:
                            CLMN_start = x
                else:
                    CLMN_counter = 0
                    CLMN_start = 0

                self.matrix[x][y] = Star(random.randint(1, 7), self.startPosStar(x, y))
                self.matrix[x][y].draw(self.screen)

                self.matrix[y][x] = Star(random.randint(2, 7), self.startPosStar(y, x))
                self.matrix[y][x].draw(self.screen)

            if STR_counter >= 3 or CLMN_counter >= 3:
                print("STR: ", STR_counter, ", CLMN: ", CLMN_counter)
