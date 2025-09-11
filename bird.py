import pygame
import math
from settings import BIRD_X, GRAVITY, JUMPS_STRENGTH

class Bird:
    def __init__(self, y):
        self.x = BIRD_X
        self.y = y
        self.start_y = y   # remember original start height
        self.velocity = 20
        self.image = pygame.image.load("assets/bee.png").convert_alpha()  # handles transparency
        # Resize the image (width=50px, height=40px for example)
        self.image = pygame.transform.scale(self.image, (50, 40))
        self.rect = self.image.get_rect()

    def update(self, elapsed_time):
        if elapsed_time < 10000:  # first 10 sec
            dynamic_gravity=0.0001*elapsed_time + 0.2  
        else:
            # normal physics after 10 sec
            dynamic_gravity = GRAVITY
            self.velocity += dynamic_gravity
            self.y += self.velocity
        self.y = max(0, min(self.y, 300 - self.rect.height))  # keep bird within screen bounds
    def jump(self):
        self.velocity = JUMPS_STRENGTH

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


