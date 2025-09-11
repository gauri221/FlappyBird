# main.py
import math
import pygame, sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from bird import Bird
from pipe import Pipe

start_time = pygame.time.get_ticks()
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

bird = Bird(SCREEN_HEIGHT // 2)
pipes = [Pipe(300), Pipe(500), Pipe(700), Pipe(900)]  # two pipes for continuity

while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.jump()
    elapsed_time = pygame.time.get_ticks() - start_time

    # Bird update
    bird.update(elapsed_time)

    for pipe in pipes:
        pipe.update()

    # Draw
    screen.fill((26, 26, 26))  
    bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)