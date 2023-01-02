import cv2
import numpy as np
from pygame.math import Vector2

from setup.setup import *


def capture_frame(cap, game):

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
