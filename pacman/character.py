import math
import pygame
from maze_matrix import MAZE_MATRIX

# Colors
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)


class Pacman:
    def __init__(self, screen, columns_amount=30, velocity=0.1):
        self._screen = screen
        self._screen_width = screen.get_width()
        self._screen_height = screen.get_height()
        self._size = self._screen_width // columns_amount
        self._column = 10
        self._row = 10
        self._radius = (self._size // 2) - 5
        self._x_position = ((self._row * self._size) + self._radius) + 3
        self._y_position = ((self._column * self._size) + self._radius) + 3
        self._x_velocity = 0
        self._y_velocity = 0
        self.__velocity = velocity
        self.oscillation = 0.3
        self.oscillation_velocity = 0.03

    def calculate(self):
        next_column = self._column + self._x_velocity
        next_row = self._row + self._y_velocity

        column_positive = math.floor(((next_column * self._size) + self._radius) / self._size)
        row_positive = math.floor(((next_row * self._size) + self._radius) / self._size)
        column_negative = math.floor(((next_column * self._size) - self._radius) / self._size)
        row_negative = math.floor(((next_row * self._size) - self._radius) / self._size)

        if (
                MAZE_MATRIX[row_positive][column_positive] != 1 and
                MAZE_MATRIX[row_negative][column_negative] != 1 and
                MAZE_MATRIX[row_negative][column_positive] != 1 and
                MAZE_MATRIX[row_positive][column_negative] != 1
        ):
            self._column = next_column
            self._row = next_row
            self._x_position = int(next_column * self._size)
            self._y_position = int(next_row * self._size)

    def turn_up(self):
        self._y_velocity = self.__velocity * -1
        self._x_velocity = 0

    def turn_down(self):
        self._y_velocity = self.__velocity
        self._x_velocity = 0

    def turn_left(self):
        self._y_velocity = 0
        self._x_velocity = self.__velocity * -1

    def turn_right(self):
        self._y_velocity = 0
        self._x_velocity = self.__velocity

    def stop_horizontal(self):
        self._x_velocity = 0

    def stop_vertical(self):
        self._y_velocity = 0

    def oscillate(self):
        if (
            self.oscillation <= 0.1 or
            self.oscillation >= 1
        ):
            self.oscillation_velocity *= -1

        self.oscillation += self.oscillation_velocity

        if self.oscillation < 0.1:
            self.oscillation = 0.1
        elif self.oscillation > 1:
            self.oscillation = 1

        print(round(self.oscillation, 1))

    def paint(self):
        self.oscillate()
        pygame.draw.circle(self._screen, YELLOW, (int(self._x_position), int(self._y_position)), self._radius)
        pygame.draw.circle(self._screen, BLACK, (int(self._x_position), int(self._y_position - 10)), 2)
        pygame.draw.polygon(self._screen, BLACK, [
            (int(self._x_position), int(self._y_position)),
            (int(self._x_position + self._radius), int(self._y_position + ((self._radius / 2 + 10) * self.oscillation))),
            (int(self._x_position + self._radius), int(self._y_position - ((self._radius / 2 + 10) * self.oscillation)))
        ])
