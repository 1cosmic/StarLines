import pygame

from stars import Star


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

        # color = (255, 255, 255)

        # V_end = start_x + self.block_w + self.space
        # H_end = start_y + self.block_w + self.space

        # V_line = (V_end, start_y)
        # H_line = (start_x, H_end)

        # while V_end - V_line[0] < self.block_margin:

           # V_end += 1
           # H_end += 1

           # V_line_end = (V_end, start_y)
           # H_line_end = (start_x, H_end)

           # pygame.draw.line(self.screen, color, V_line, V_line_end, self.line_w)
           # pygame.draw.line(self.screen, color, H_line, H_line_end, self.line_w)
           # pygame.display.update()



        # JOB CODE!

        color = (255, 255, 255)

        # Draw line, who separate of star_block.
        startPos = (start_x, start_y)

        endPos = (start_x, start_y + height)
        pygame.draw.line(self.screen, color, startPos, endPos, width)


    def draw_star(self):
        pass

    def draw(self, win_size):
        """Draw field in surface."""

        self.block_w = 60
        self.line_w = 2
        self.space = 6

        self.block_margin = self.block_w + self.space
        self.line_l = (self.block_margin + self.line_w) * 9

        pos_x = (win_size[0] - self.line_l) / 2
        pos_y = (win_size[1] - self.line_l) / 2  # set up start position.

        # Draw is step-to-step for stars on screen.
        for line in self.matrix:

            # Draw block.
            self.draw_star_block(pos_x, pos_y)

            # Draw separate line.
            self.draw_line(pos_x, pos_y)

            # Animated draw.
            pygame.time.delay(5)
            pygame.display.update()

            pos_x += self.block_margin


    def add_Star(self, x, y, colorID):
        self.matrix[x][y] = Star(colorID, coordsXY(x, y))


    @staticmethod
    coordsXY(x, y):

