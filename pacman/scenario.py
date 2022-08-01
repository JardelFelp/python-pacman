import pygame
import copy
from maze_matrix import MAZE_MATRIX

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


class Scenario:
    def __init__(self, screen, column_amount=30):
        self._screen = screen
        self._column_amount = column_amount
        self._maze_matrix = copy.deepcopy(MAZE_MATRIX)
        self._screen_height = screen.get_height()
        self._screen_width = screen.get_width()
        self._size = self._screen_width // column_amount

    def generate_maze(self):
        for row_index, row in enumerate(self._maze_matrix):
            for column_index, column in enumerate(row):
                color = BLUE if column == 1 else BLACK
                pygame.draw.rect(self._screen, color, (
                    int(column_index * self._size),
                    int(row_index * self._size),
                    self._size,
                    self._size
                ))
