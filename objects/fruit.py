import random

import pygame
from pygame.math import Vector2

from constants import CELL_NUMBER, CELL_SIZE


class Fruit:
    def __init__(self, game):
        self.game = game
        self.randomize()
        self.load_assets()

    def load_assets(self):
        self.image = pygame.image.load('assets/fruit.png').convert_alpha()

    def draw(self):
        rectangle = pygame.Rect(int(self.x * CELL_SIZE),
                                int(self.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        self.game.screen.blit(self.image, rectangle)

    def randomize(self):
        while True:
            self.x = random.randint(0, CELL_NUMBER - 1)
            self.y = random.randint(0, CELL_NUMBER - 1)
            if Vector2(self.x, self.y) not in self.game.snake.body:
                self.position = Vector2(self.x, self.y)
                break
