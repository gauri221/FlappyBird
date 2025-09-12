import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PIPE_SPEED

class Obstacle:
    used_positions = []  # to avoid vertical overlap

    def __init__(self, x):
        # Load images
        self.images = [
            pygame.image.load("assets/alien.png").convert_alpha(),
            pygame.image.load("assets/bluealien.png").convert_alpha(),
            pygame.image.load("assets/oneEyeAlien.png").convert_alpha(),
            pygame.image.load("assets/orangeAlien.png").convert_alpha(),
            pygame.image.load("assets/satellite.png").convert_alpha()
        ]

        # Pick random image
        self.image = random.choice(self.images)

        # Bigger scaling
        MAX_WIDTH, MAX_HEIGHT = 120, 120
        self.image = pygame.transform.scale(self.image, (MAX_WIDTH, MAX_HEIGHT))

        # Rect
        self.rect = self.image.get_rect()
        self.rect.x = x

        # Random y, avoiding overlaps
        self.rect.y = self.get_non_overlapping_y()

        # Speed
        self.speed = PIPE_SPEED

        # Flag to prevent appearing near rocket in first 5 sec
        self.safe_zone_active = True

    def get_non_overlapping_y(self):
        """Pick a y position that doesn't overlap existing obstacles"""
        attempts = 0
        while True:
            y = random.randint(50, SCREEN_HEIGHT - 150)
            if all(abs(y - pos) > 100 for pos in Obstacle.used_positions):
                Obstacle.used_positions.append(y)
                return y
            attempts += 1
            if attempts > 50:  # fallback
                return y

    def update(self, elapsed_time):
        # For first 5 seconds, keep obstacles away from rocket
        if elapsed_time < 5000:
            # move obstacles more slowly, or keep them off-screen initially
            self.rect.x -= self.speed * 0.5  # slower movement
        else:
            self.rect.x -= self.speed

        if self.rect.right < 0:
            self.reset()

    def reset(self):
        """Reposition obstacle off-screen smoothly"""
        self.image = random.choice(self.images)
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH  # start from right end
        self.rect.y = self.get_non_overlapping_y()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
