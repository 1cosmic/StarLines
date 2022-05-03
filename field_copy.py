import pygame
import os



class Field():

    def __init__(self, screen):
        self.screen = screen
        self.matrix = [[0] * 9 for i in range(9)]


        # Самым оптимальным будет помещение звезды как айдишник в поле выше.
        # Таким образом, обращаясь к определённому индексу в матрице, мы
        # сможем зафиксировать её жёсткое положение на игровом поле, изменить
        # фон звезды и прочее.
        #
        # Сделать по матрице:
        # 1. Сделать что-то в роде рамок / полок и прочего для звёзд.
        # 3. Добавить поле "color_id" для последующей связки звезда - ячейка.
        #
        # Сделать по звёздам:
        # 1. Гифки (спрайты) для 7 цветов звезд.
        # 2. Механизм выбора и перемещения звезд.
        #


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

        # Draw separate line.
        self.draw_line(pos_x, pos_y)

        # Draw is step-to-step for stars on screen.
        for line in self.matrix:

            # Draw block.
            self.draw_star_block(pos_x, pos_y)


            # Animated draw.
            pygame.time.delay(10)
            pygame.display.update()
