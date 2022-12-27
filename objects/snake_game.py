import pygame

from constants import *
from objects.fruit import *
from objects.snake import *


class SnakeGame:
    def __init__(self, screen):
        self.screen = screen
        self.snake = Snake(self)
        self.fruit = Fruit(self)
        self.font = pygame.font.Font("assets/PoetsenOne-Regular.ttf", 25)

    def update(self):
        self.snake.move()
        self.check_collision()
        self.check_fail()

    def draw(self):
        self.draw_background()
        self.snake.draw()
        self.fruit.draw()
        self.draw_score()

    def draw_background(self):
        for row in range(CELL_NUMBER):
            if row % 2 == 0:
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        rectangle = pygame.Rect(
                            col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(
                            self.screen, dark_green, rectangle)
            else:
                for col in range(CELL_NUMBER):
                    if col % 2 != 0:
                        rectangle = pygame.Rect(
                            col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(
                            self.screen, dark_green, rectangle)

    def draw_score(self):
        score = len(self.snake.body) - 3
        surface = self.font.render(f"Score:  {score}", True, BLACK)
        self.screen.blit(surface, (CELL_SIZE/2, CELL_SIZE/2))

    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.append_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < CELL_NUMBER or not 0 <= self.snake.body[0].y < CELL_NUMBER:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.time.delay(500)
        self.snake.reset()
