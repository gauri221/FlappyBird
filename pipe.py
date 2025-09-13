# pipe.py
import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PIPE_GAP, PIPE_SPEED

class Pipe:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 60
        self.gap = PIPE_GAP

        self.top_height = random.randint(50, SCREEN_HEIGHT - self.gap - 50) # Randomize top pipe height
        self.image = pygame.image.load("assets/pipsie.png").convert_alpha() # Load pipe image
        self.image = pygame.transform.scale(self.image, (self.width, SCREEN_HEIGHT)) # Scale pipe width, keep screen height
        # Create rects for top and bottom pipes

        self.top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        self.bottom_rect = pygame.Rect(self.x, self.top_height + self.gap, self.width, SCREEN_HEIGHT - (self.top_height + self.gap))

        # self.top_rect = self.image.get_rect(
        #     bottomleft=(self.x, self.top_height)
        # )
        # self.bottom_rect = self.image.get_rect(
        #     topleft=(self.x, self.top_height + self.gap)
        # )

    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x -= PIPE_SPEED
        self.bottom_rect.x -= PIPE_SPEED

        if self.x + self.width < 0:
            self.x = SCREEN_WIDTH
            self.top_height = random.randint(50, SCREEN_HEIGHT - self.gap - 50)
            self.top_rect.bottomleft = (self.x, self.top_height)
            self.bottom_rect.topleft = (self.x, self.top_height + self.gap)
            if hasattr(self, "scored"):
                del self.scored   # 🔑 allow scoring again

    def draw(self, screen):
        # Top pipe (flipped vertically)
        top_pipe = pygame.transform.flip(self.image, False, True)
        screen.blit(top_pipe, (self.x, self.top_height - SCREEN_HEIGHT))

        # Bottom pipe (normal)
        screen.blit(self.image, (self.x, self.top_height + self.gap))
