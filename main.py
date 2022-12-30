import sys
from threading import Thread

import cv2
import numpy as np
import pygame
from pygame.math import Vector2

from objects.snake_game import *
from setup.setup import *


def worker(cap, game):

    _, frame = cap.read()
    if frame is None:
        return

    x, y, c = frame.shape

    frame = cv2.flip(frame, 1)

    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(framergb)

    className = ''

    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

        prediction = model.predict([landmarks])

        if (np.max(prediction) > 0.99):
            className = classNames[np.argmax(prediction)]

    if className == 'thumbs up':
        if game.snake.direction.y != 1:
            game.snake.direction = Vector2(0, -1)
    elif className == 'thumbs down':
        if game.snake.direction.y != -1:
            game.snake.direction = Vector2(0, 1)
    elif className == 'fist':
        if game.snake.direction.x != -1:
            game.snake.direction = Vector2(1, 0)
    elif className == 'okay':
        if game.snake.direction.x != 1 and game.snake.direction != Vector2(0, 0):
            game.snake.direction = Vector2(-1, 0)

    if className != '':
        print(className)


def main():
    global direction
    threads = []

    cap = cv2.VideoCapture(0)

    pygame.init()
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode(
        (CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
    clock = pygame.time.Clock()

    game = SnakeGame(screen)

    CAPTURE_FRAME = pygame.USEREVENT
    pygame.time.set_timer(CAPTURE_FRAME, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                cap.release()
                cv2.destroyAllWindows()

                pygame.quit()
                sys.exit()

            if event.type == CAPTURE_FRAME:
                t = Thread(target=worker, args=(cap, game))
                threads.append(t)
                t.daemon = True
                t.start()

        if game.reset:
            for thread in threads:
                thread.join()
            threads = []
            game.reset = False

        screen.fill(light_green)
        game.update()
        game.draw()
        pygame.display.update()
        clock.tick_busy_loop(FPS)


if __name__ == "__main__":
    main()
