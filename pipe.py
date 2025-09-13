# pipe.py
import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PIPE_GAP, PIPE_SPEED

class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 60
        self.gap = PIPE_GAP

        # Randomize top pipe height
        self.top_height = random.randint(50, SCREEN_HEIGHT - self.gap - 50)

        # Load pipe image
        self.image = pygame.image.load("assets/pipsie.png").convert_alpha()

        # Scale pipe width, keep screen height
        self.image = pygame.transform.scale(self.image, (self.width, SCREEN_HEIGHT))

    def update(self):
        self.x -= PIPE_SPEED
        if self.x + self.width < 0:
            self.x = SCREEN_WIDTH
            self.top_height = random.randint(50, SCREEN_HEIGHT - self.gap - 50)

    def draw(self, screen):
        # Top pipe (flipped vertically)
        top_pipe = pygame.transform.flip(self.image, False, True)
        screen.blit(top_pipe, (self.x, self.top_height - SCREEN_HEIGHT))

        # Bottom pipe (normal)
        screen.blit(self.image, (self.x, self.top_height + self.gap))
