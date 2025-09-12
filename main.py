# main.py
import math
import pygame, sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from bird import Rocket
from pipe import Obstacle

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

start_time = pygame.time.get_ticks()

# Load background
background = pygame.image.load("assets/space.jpg").convert_alpha()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize rocket
rocket = Rocket(SCREEN_HEIGHT // 2)

# Initialize obstacles
obstacles = [Obstacle(x) for x in [400, 700, 1000]]

while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            rocket.jump()

    # Elapsed time
    elapsed_time = pygame.time.get_ticks() - start_time

    # Rocket update (pass elapsed_time if needed)
    rocket.update(elapsed_time)

    # Update obstacles with elapsed_time
    for obstacle in obstacles:
        obstacle.update(elapsed_time)

    # Draw everything
    screen.blit(background, (0, 0))
    rocket.draw(screen)
    for obstacle in obstacles:
        # Skip drawing near rocket in first 5 seconds
        if elapsed_time < 5000 and obstacle.rect.x < 200:  # adjust 200 for rocket x
            continue
        obstacle.draw(screen)

    # Refresh screen
    pygame.display.flip()
    clock.tick(FPS)
