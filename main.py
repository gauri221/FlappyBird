# main.py
import pygame, sys
from pygame import mixer, time
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from bird import Bird
from pipe import Pipe

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

font = pygame.font.Font(None, 48)  # default font, size 48
score = 0
game_over = False

# Load background
background = pygame.image.load("assets/sky.jpg").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize bird
bird = Bird(100, SCREEN_HEIGHT // 2)

# Initialize pipes
pipes = [Pipe(x, y=0) for x in [400, 700, 1000]]


mixer.init()
# Loading the song
mixer.music.load("assets/Una_Paloma_Blanca.mp3")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play(-1) # loop indefinitely

def show_game_over_screen():
    # screen.fill((0, 0, 0))
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    score_text = font.render(f"Final Score: {score}", True, (143, 45, 86))
    restart_text = font.render("Press ENTER to Restart or ESC to Quit", True, (143, 45, 86))

    screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, 150))
    screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 200))
    screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, 300))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    waiting = False


while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.jump()

    elapsed_time = pygame.time.get_ticks() - start_time  
    bird_hitbox = bird.rect.inflate(-20, -20)  # shrink by 5px on all sides

    # Update
    bird.update(elapsed_time)
    for pipe in pipes:
        pipe.update()
        top_hitbox = pipe.top_rect.inflate(-15, -15)
        bottom_hitbox = pipe.bottom_rect.inflate(-15, -15)

        
        if (bird_hitbox.colliderect(top_hitbox) or
            bird_hitbox.colliderect(bottom_hitbox) or
            bird.rect.top <= 0 or bird.rect.bottom >= SCREEN_HEIGHT):
            game_over = True
            mixer.music.stop()
            mixer.music.load("assets/game_over.mp3")
            mixer.music.play()

        # Scoring: when pipe passes the bird
        if not game_over and pipe.x + pipe.width < bird.rect.x and not hasattr(pipe, "scored"):
            score += 1
            pipe.scored = True  # mark pipe as counted

        if game_over:
            show_game_over_screen()
            # reset game state
            bird = Bird(100, SCREEN_HEIGHT // 2)
            pipes = [Pipe(x, y=0) for x in [400, 700, 1000]]
            score = 0
            game_over = False
            mixer.music.load("assets/Una_Paloma_Blanca.mp3")
            mixer.music.play(-1)


    # Draw everything
    screen.blit(background, (0, 0))
    bird.draw(screen)
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surface, (20, 20))
    for pipe in pipes:
        pipe.draw(screen)

    # Refresh screen
    pygame.display.flip()
    clock.tick(FPS)
