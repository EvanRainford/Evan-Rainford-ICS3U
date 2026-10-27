import pygame
import random

pygame.init()

screen = pygame.display.set.mode ((600, 600))
pygame.display.set_caption("Tile frenzy")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 65)
tiles = []

for row in range(3):
    x = 120 + col * 125
    y = 120 + col * 125
    tiles.append(pygame.Rect(x, y, 110, 110))

score = 0
target = random.randint(0, 8)
time_left = 30
game_state = "start"
start_time = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    for tile in tiles:
        pygame.draw.rect(screen, (170, 170, 170,), tile)

pygame.display.update()
clock.tick(60)

pygame.quit()
