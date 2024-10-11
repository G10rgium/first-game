import sys

import pygame

from controller import Player

pygame.init()


WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_1 = Player()

running = True

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, BLACK, (player_1.x, player_1.y, player_1.size, player_1.size))
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
    player_1.move_player(dx, dy)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()





