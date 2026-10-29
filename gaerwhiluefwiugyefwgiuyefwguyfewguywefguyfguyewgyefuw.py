import pygame
import random

pygame.init()

# Screen
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tile Frenzy")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 225)
GREEN = (0, 255, 0)

# Font
font = pygame.font.SysFont(None, 40)

# Create tiles
tiles = []
for row in range(3):
    for col in range(3):
        x = 120 + col * 125
        y = 120 + row * 125
        tiles.append(pygame.Rect(x, y, 110, 110))

# Game variables
score = 0
target = random.randint(0, 8)
time_left = 30
game_state = "start"
start_time = 0

running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if game_state == "start":
                score = 0
                target = random.randint(0, 8)
                start_time = pygame.time.get_ticks()
                game_state = "play"

            elif game_state == "play":
                if tiles[target].collidepoint(event.pos):
                    score += 1
                    target = random.randint(0, 8)

            elif game_state == "over":
                game_state = "start"

    # Start Screen
    if game_state == "start":
        title = font.render("TILE FRENZY", True, BLACK)
        message = font.render("Click to Start", True, BLACK)

        screen.blit(title, (180, 220))
        screen.blit(message, (180, 280))

    # Game Screen
    elif game_state == "play":

        seconds = (pygame.time.get_ticks() - start_time) // 1000
        time_left = 30 - seconds

        if time_left <= 0:
            time_left = 0
            game_state = "over"

        for i in range(9):
            color = GREEN if i == target else BLUE
            pygame.draw.rect(screen, color, tiles[i])

        score_text = font.render(f"Score: {score}", True, BLACK)
        time_text = font.render(f"Time: {time_left}", True, BLACK)

        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 50))

    # Game Over Screen
    elif game_state == "over":
        game_over = font.render("GAME OVER", True, BLACK)
        score_text = font.render(f"Final Score: {score}", True, BLACK)
        restart_text = font.render("Click to Restart", True, BLACK)

        screen.blit(game_over, (170, 200))
        screen.blit(score_text, (160, 260))
        screen.blit(restart_text, (140, 320))

    pygame.display.update()
    clock.tick(60)

pygame.quit()