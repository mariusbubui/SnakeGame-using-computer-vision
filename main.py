import sys
from threading import Thread

import cv2
import pygame

from objects.snake_game import *
from setup.setup import *
from video_capture import capture_frame


def main():
    threads = []
    cap = cv2.VideoCapture(0)

    pygame.init()
    pygame.display.set_caption("Snake")
    screen = pygame.display.set_mode(
        (CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
    clock = pygame.time.Clock()

    game = SnakeGame(screen)

    CAPTURE_FRAME = pygame.USEREVENT
    pygame.time.set_timer(CAPTURE_FRAME, CAPTURE_FRAME_INTERVAL)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                cap.release()
                cv2.destroyAllWindows()

                pygame.quit()
                sys.exit()

            if event.type == CAPTURE_FRAME:
                t = Thread(target=capture_frame, args=(cap, game))
                threads.append(t)
                t.daemon = True
                t.start()

        if game.reset:
            for thread in threads:
                thread.join()
            threads = []
            game.reset = False

        screen.fill(LIGHT_GREEN)
        game.update()
        game.draw()
        pygame.display.update()
        clock.tick_busy_loop(FPS)


if __name__ == "__main__":
    main()
