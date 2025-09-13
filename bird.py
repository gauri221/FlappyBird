# bird.py
import pygame
from settings import GRAVITY, JUMP_STRENGTH

class Bird:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/bird.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 60))  # nice size
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = 0

    def update(self, elapsed_time):
        if elapsed_time < 5000:  # first 10 sec
            dynamic_gravity = 0.0001 * elapsed_time
            self.velocity += dynamic_gravity
            self.rect.y += self.velocity
        else:
            dynamic_gravity = GRAVITY  # fallback to the one from settings
            self.velocity += dynamic_gravity
            self.rect.y += self.velocity

    def jump(self):
        self.velocity = JUMP_STRENGTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)
