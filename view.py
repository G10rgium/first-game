import sys

import pygame
from pygame.examples.video import backgrounds

from controller import Player

pygame.init()


background_image = pygame.image.load("tortoise.png")


WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_1 = Player()

pygame.display.set_caption("user: ")

font = pygame.font.SysFont('Arial', 30)
username = ""

running = True

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_DOWN:
            username += event.unicode
    # pygame.draw.rect(screen, BLACk, (player_1.x, player_1.y, player_1.size, player_1.size))
    screen.blit(pygame.transform.scale(background_image, (player_1.size, player_1.size)), (player_1.x, player_1.y))
    keyboard = pygame.key.get_pressed()
    # print(keyboard)
    dx = 0
    dy = 0
    if keyboard[pygame.K_LEFT]:
        dx -= 1
    if keyboard[pygame.K_RIGHT]:
        dx += 1
    if keyboard[pygame.K_UP]:
        dy -= 1
    if keyboard[pygame.K_DOWN]:
        dy += 1

    username_screen = font.render(username, True, RED)
    screen.blit(username_screen, (player_1.x, player_1.y + 50))


    player_1.move_player(dx, dy)
    pygame.display.update()
    clock.tick(30)

print(username)

pygame.quit()
sys.exit()





