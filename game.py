import pygame 
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Dodge The Blocks")
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (220,50, 50)
blue = (0, 120, 225)

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)

player = pygame.Rect(275, 530, 50, 50)
blocks = []
spawn_timer = 0
game_over = False
running = True

def reset_game():
    player.x = 275
    blocks.clear()
    return 0, 0, False  

def add_block():   
    x = random.randint(0, 550)
    blocks.append(pygame.Rect(x, -50, 50, 50))

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                score, spawn_timmer, game_over = reset_game()
    if not game_over:
        keys = pygame.key.get.pressed()
