# main.py
import pygame, sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from bird import Bird
from pipe import Pipe

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()


# Load background
background = pygame.image.load("assets/sky.jpg").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize bird
bird = Bird(100, SCREEN_HEIGHT // 2)

# Initialize pipes
pipes = [Pipe(x) for x in [400, 700, 1000]]

while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.jump()

    elapsed_time = pygame.time.get_ticks() - start_time  

    # Update
    bird.update(elapsed_time)
    for pipe in pipes:
        pipe.update()

    # Draw everything
    screen.blit(background, (0, 0))
    bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)

    # Refresh screen
    pygame.display.flip()
    clock.tick(FPS)
