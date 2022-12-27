import pygame
from pygame.math import Vector2

from constants import CELL_SIZE


class Snake:
    def __init__(self, game):
        self.game = game
        self.body = [Vector2(7, 9), Vector2(6, 9), Vector2(5, 9)]
        self.direction = pygame.math.Vector2(0, 0)
        self.append = False
        self.load_assets()

    def load_assets(self):
        self.head_up = pygame.image.load('assets/head_up.png').convert_alpha()
        self.head_down = pygame.image.load(
            'assets/head_down.png').convert_alpha()
        self.head_right = pygame.image.load(
            'assets/head_right.png').convert_alpha()
        self.head_left = pygame.image.load(
            'assets/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('assets/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(
            'assets/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(
            'assets/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(
            'assets/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load(
            'assets/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(
            'assets/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('assets/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('assets/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('assets/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('assets/body_bl.png').convert_alpha()

    def draw(self):
        for index, block in enumerate(self.body):
            x = int(block.x * CELL_SIZE)
            y = int(block.y * CELL_SIZE)
            rectangle = pygame.Rect(
                x, y, CELL_SIZE, CELL_SIZE)

            if index == 0:
                self.update_head(rectangle)
            elif index == len(self.body) - 1:
                self.update_tail(rectangle)
            else:
                self.update_body(index, block, rectangle)

    def update_head(self, rectangle):
        head_direction = self.body[1] - self.body[0]

        if head_direction == Vector2(1, 0):
            self.game.screen.blit(self.head_left, rectangle)
        elif head_direction == Vector2(-1, 0):
            self.game.screen.blit(self.head_right, rectangle)
        elif head_direction == Vector2(0, 1):
            self.game.screen.blit(self.head_up, rectangle)
        elif head_direction == Vector2(0, -1):
            self.game.screen.blit(self.head_down, rectangle)

    def update_tail(self, rectangle):
        tail_direction = self.body[-2] - self.body[-1]

        if tail_direction == Vector2(1, 0):
            self.game.screen.blit(self.tail_left, rectangle)
        elif tail_direction == Vector2(-1, 0):
            self.game.screen.blit(self.tail_right, rectangle)
        elif tail_direction == Vector2(0, 1):
            self.game.screen.blit(self.tail_up, rectangle)
        elif tail_direction == Vector2(0, -1):
            self.game.screen.blit(self.tail_down, rectangle)

    def update_body(self, index, block, rectangle):
        previous_block = self.body[index + 1] - block
        next_block = self.body[index - 1] - block
        if previous_block.x == next_block.x:
            self.game.screen.blit(self.body_vertical, rectangle)
        elif previous_block.y == next_block.y:
            self.game.screen.blit(self.body_horizontal, rectangle)
        else:
            if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                self.game.screen.blit(self.body_tl, rectangle)
            elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                self.game.screen.blit(self.body_bl, rectangle)
            elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                self.game.screen.blit(self.body_tr, rectangle)
            elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                self.game.screen.blit(self.body_br, rectangle)

    def move(self):
        if self.direction != Vector2(0, 0):
            if self.append:
                self.append = False
                copy = self.body[:]
                copy.insert(0, copy[0] + self.direction)
                self.body = copy[:]
            else:
                copy = self.body[:-1]
                copy.insert(0, copy[0] + self.direction)
                self.body = copy[:]

    def append_block(self):
        self.append = True

    def reset(self):
        self.body = [Vector2(7, 9), Vector2(6, 9), Vector2(5, 9)]
        self.direction = pygame.math.Vector2(0, 0)
        self.append = False
