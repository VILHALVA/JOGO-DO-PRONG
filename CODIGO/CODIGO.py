import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("JOGO DO PRONG")

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

ball_x = SCREEN_WIDTH / 2
ball_y = SCREEN_HEIGHT / 2
ball_size = 20
ball_speed_x = 3
ball_speed_y = 3

player_x = SCREEN_WIDTH / 2
player_y = SCREEN_HEIGHT - 100
player_size = 40

enemy_x = SCREEN_WIDTH / 2
enemy_y = SCREEN_HEIGHT / 2
enemy_size = 60
enemy_speed_x = 7
enemy_speed_y = 7

ball_growth = -2
player_speed = 5
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    if ball_y + ball_size / 2 > SCREEN_HEIGHT or ball_y - ball_size / 2 < 0:
        ball_speed_y = -ball_speed_y
    if ball_x + ball_size / 2 > SCREEN_WIDTH or ball_x - ball_size / 2 < 0:
        ball_speed_x = -ball_speed_x

    if (ball_x + ball_size / 2 > player_x - player_size / 2 and
        ball_x - ball_size / 2 < player_x + player_size / 2 and
        ball_y + ball_size / 2 > player_y - player_size / 2 and
        ball_y - ball_size / 2 < player_y + player_size / 2):
        
        ball_x = SCREEN_WIDTH / 2
        ball_y = SCREEN_HEIGHT / 2
        player_size += 8.5
        enemy_speed_x += 2.5
        enemy_speed_y += 2.5

        if player_size >= 200:
            player_size = 200

    enemy_x += enemy_speed_x
    enemy_y += enemy_speed_y
    
    if enemy_x + enemy_size / 2 > SCREEN_WIDTH or enemy_x - enemy_size / 2 < 0:
        enemy_speed_x = -enemy_speed_x
    if enemy_y + enemy_size / 2 > SCREEN_HEIGHT or enemy_y - enemy_size / 2 < 0:
        enemy_speed_y = -enemy_speed_y

    if (player_x + player_size / 2 > enemy_x - enemy_size / 2 and
        player_x - player_size / 2 < enemy_x + enemy_size / 2 and
        player_y + player_size / 2 > enemy_y - enemy_size / 2 and
        player_y - player_size / 2 < enemy_y + enemy_size / 2):
        
        player_size += ball_growth
        if player_size <= 10:
            player_size = 10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if player_x < player_size / 2:
        player_x = player_size / 2
    if player_x > SCREEN_WIDTH - player_size / 2:
        player_x = SCREEN_WIDTH - player_size / 2
    if player_y < player_size / 2:
        player_y = player_size / 2
    if player_y > SCREEN_HEIGHT - player_size / 2:
        player_y = SCREEN_HEIGHT - player_size / 2

    screen.fill(BLACK)

    pygame.draw.ellipse(screen, GREEN, (ball_x - ball_size / 2, ball_y - ball_size / 2, ball_size, ball_size))
    pygame.draw.rect(screen, BLUE, (player_x - player_size / 2, player_y - player_size / 2, player_size, player_size))
    pygame.draw.rect(screen, RED, (enemy_x - enemy_size / 2, enemy_y - enemy_size / 2, enemy_size, enemy_size))

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
