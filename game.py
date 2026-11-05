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
score = 0
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
                score, spawn_timer, game_over = reset_game()
    if not game_over:
        keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5

    if keys[pygame.K_RIGHT]:
        player.x += 5

    if player.x < 0:
        player.x = 0

    if player.x > 550:
        player.x = 550

    spawn_timer += 1

    if spawn_timer >= 30:
        add_block()
        spawn_timer = 0

    for block in blocks[:]:
        block.y += 5

        if block.y > 600:
            blocks.remove(block)
            score += 1

        elif player.colliderect(block):
            game_over = True

    screen.fill(white)

    pygame.draw.rect(screen, blue, player)

    for block in blocks:
        pygame.draw.rect(screen, red, block)

    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))

    if game_over:
        game_text = font.render("GAME OVER", True, black)
        screen.blit(game_text, (200, 250))

        restart_text = small_font.render("Press R to restart", True, black)
        screen.blit(restart_text, (200, 300))

    pygame.display.update()

pygame.quit()