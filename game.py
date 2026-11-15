
import pygame
import random
import os
pygame.init()

pygame.mixer.init()

if os.path.exists("musicc.mp3"):
    pygame.mixer.music.load("musicc.mp3")
    pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Dodge The Snowflakes")
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (220, 50, 50)
blue = (0, 120, 225)
green = (0, 200, 90)

background = pygame.image.load("christmas_background.png").convert()
background = pygame.transform.scale(background, (600, 600))

snowflake_image = pygame.image.load("snowflake.png").convert_alpha()
snowflake_image = pygame.transform.scale(snowflake_image, (50, 50))

red_present = pygame.image.load("present_red.png").convert_alpha()
red_present = pygame.transform.scale(red_present, (40, 40))

green_present = pygame.image.load("present_green.png").convert_alpha()
green_present = pygame.transform.scale(green_present, (40, 40))

blue_present = pygame.image.load("present_blue.png").convert_alpha()
blue_present = pygame.transform.scale(blue_present, (40, 40))

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)

player = pygame.Rect(275, 530, 50, 50)
blocks = []
presents = []
spawn_timer = 0
present_timer = 0
score = 0
game_over = False
running = True
block_speed = 5
shield = False
slow_timer = 0

def reset_game():
    player.x = 275
    blocks.clear()
    presents.clear()
    return 0, 0, False, 0, False, 0

def add_block():
    x = random.randint(0, 550)
    blocks.append(pygame.Rect(x, -50, 50, 50))

def add_present():
    x = random.randint(0, 560)
    color = random.choice(["red", "green", "blue"])
    presents.append([pygame.Rect(x, -40, 40, 40), color])


while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                score, spawn_timer, game_over, present_timer, shield, slow_timer = reset_game()

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

        if slow_timer > 0:
            slow_timer -= 1

        block_speed = 5 + (score // 10)

        if slow_timer > 0:
            block_speed -= 3
            if block_speed < 2:
                block_speed = 2

        spawn_timer += 1
        present_timer += 1

        if spawn_timer >= 30:
            add_block()
            spawn_timer = 0

        if present_timer >= 300:
            add_present()
            present_timer = 0

        for present in presents[:]:
            present[0].y += 3

            if present[0].y > 600:
                presents.remove(present)

            elif player.colliderect(present[0]):
                if present[1] == "red":
                    score += 5

                if present[1] == "green":
                    shield = True

                if present[1] == "blue":
                    slow_timer = 300

                presents.remove(present)

        for block in blocks[:]:
            block.y += block_speed

            if block.y > 600:
                blocks.remove(block)
                score += 1

            elif player.colliderect(block):
                if shield:
                    blocks.remove(block)
                    shield = False
                else:
                    game_over = True
                    break

    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, blue, player)

    if shield:
        pygame.draw.rect(screen, green, player, 5)

    for block in blocks:
        screen.blit(snowflake_image, (block.x, block.y))

    for present in presents:
        if present[1] == "red":
            screen.blit(red_present, (present[0].x, present[0].y))

        if present[1] == "green":
            screen.blit(green_present, (present[0].x, present[0].y))

        if present[1] == "blue":
            screen.blit(blue_present, (present[0].x, present[0].y))

    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))

    power_text = small_font.render("Red +5   Green Shield   Blue Slow", True, black)
    screen.blit(power_text, (10, 55))

    if shield:
        shield_text = small_font.render("Shield: ON", True, black)
        screen.blit(shield_text, (10, 90))

    if slow_timer > 0:
        slow_text = small_font.render("Slow: " + str(slow_timer // 60 + 1) + "s", True, black)
        screen.blit(slow_text, (10, 120))

    if game_over:
        game_text = font.render("GAME OVER", True, black)
        screen.blit(game_text, (200, 250))

        restart_text = small_font.render("Press R to restart", True, black)
        screen.blit(restart_text, (200, 300))

    pygame.display.update()

pygame.quit()
