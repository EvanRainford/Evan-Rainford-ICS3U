import pygame
import random

pygame.init()

screen = pygame.display.set_mode ((600, 600))
pygame.display.set_caption("Tile frenzy")

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0,)
blue = (0, 150, 225)
green = (0, 255, 0)
tile_x = random.randint(0, 700)
tile_y = random.randint(0, 500)
tile_size = 100
font = pygame.font.SysFont(None, 40)

tiles = []

for row in range(3):
   for col in range(3):
        x = 120 + col * 125
        y = 120 + row * 125
        tiles.append(pygame.Rect(x, y, 110, 110))

score = 0
target = random.randint(0, 8)
time_left = 30
game_state = "start"
start_time = 0
running = True

while running:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:    
           
          if game_state == "start":
            score = 0
            target = random.randint(0, 8)
            start_time = pygame.time.get_ticks()
            game_state = "play" 

        elif game_state == "over":
            game_state = "start"

if game_state == "start":
    title = font.render("TILE FRENZY", True, black)
    message = font.render("Click to Start", True, black)

    screen.blit(title, (200, 200))
    screen.blit(message, (190, 300))

elif game_state == "play":
    mouse_pos =pygame.mouse.get_pos()
    if tiles[target].collidepoint(mouse_pos):
        score += 1
        target = random.randint(0, 8)
    seconds = (pygame.time.get_ticks() - start_time) // 1000
    time_left = 30 - seconds

    if time_left <= 0:
        time_left = 0
        game_state = "over"

    for i in range(9):
        if i == target:
            pygame.draw.rect(screen, green, tiles[i])
        else:
            pygame.draw.rect(screen, blue, tiles[i])
    score_text = font.render("score: " + str(score), True, black)
    time_text = font.render("time: " + str(time_left), True, black)
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))

    pygame.display.update()
    clock.tick(60)

    pygame.quit()
