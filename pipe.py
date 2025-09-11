# pipe.py
import pygame
import random
import math
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PIPE_GAP, PIPE_SPEED

class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 60
        self.gap = PIPE_GAP
        self.top_height = random.randint(50, SCREEN_HEIGHT - self.gap - 50)

    def update(self):
        self.x -= PIPE_SPEED
        if self.x + self.width < 0:
            self.x = SCREEN_WIDTH
            self.top_height = random.randint(50, SCREEN_HEIGHT - self.gap - 50)

    def draw(self, screen):
        # Top pipe
        pygame.draw.rect(screen, (247,247,247), (self.x, 0, self.width, self.top_height))
        # Bottom pipe
        bottom_y = self.top_height + self.gap
        pygame.draw.rect(screen, (247,247,247), (self.x, bottom_y, self.width, SCREEN_HEIGHT - bottom_y))