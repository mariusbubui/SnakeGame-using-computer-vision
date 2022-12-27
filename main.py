import sys

import pygame
from pygame.math import Vector2

from objects.snake_game import *


def main():
    pygame.init()
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode(
        (CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
    clock = pygame.time.Clock()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 125)

    game = SnakeGame(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == SCREEN_UPDATE:
                game.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if game.snake.direction.y != 1:
                        game.snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_DOWN:
                    if game.snake.direction.y != -1:
                        game.snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_RIGHT:
                    if game.snake.direction.x != -1:
                        game.snake.direction = Vector2(1, 0)
                elif event.key == pygame.K_LEFT:
                    if game.snake.direction.x != 1 and game.snake.direction != Vector2(0, 0):
                        game.snake.direction = Vector2(-1, 0)

        screen.fill(light_green)
        game.draw()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
