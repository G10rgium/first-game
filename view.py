import sys

import pygame

from random import randint

from controller import Player, Bamboo, Player2

pygame.init()

background_image = pygame.image.load("background_1.png")

player_image = pygame.image.load("panda-bear.png")

hunter = pygame.image.load("lumberjack.png")

hunter_1 = Player2()

WIDTH = 1920
HEIGHT = 1080

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_1 = Player()

pygame.display.set_caption("user: ")

# font = pygame.font.SysFont('Arial', 30)
# username = ""

running = True

bamboo = pygame.image.load("bamboo.png")

# pixel = 64

bambo = Bamboo()


while running:
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





        # if event.type == pygame.KEYDOWN:
        #     username += event.unicode
    # pygame.draw.rect(screen, BLACk, (player_1.x, player_1.y, player_1.size, player_1.size))
    screen.blit(pygame.transform.scale(player_image, (player_1.size, player_1.size)), (player_1.x, player_1.y))
    screen.blit(pygame.transform.scale(bamboo, (bambo.size, bambo.size)), (bambo.x, bambo.y))
    screen.blit(pygame.transform.scale(hunter, (hunter_1.size, hunter_1.size)), (hunter_1.x, hunter_1.y))
    keyboard = pygame.key.get_pressed()
    # print(keyboard)
    if player_1.x == hunter_1.x and player_1.y == hunter_1.y:
        running = False
    dx = 0
    dy = 0
    wx = 0
    wy = 0
    def update():
        if keyboard[pygame.K_LEFT] and player_1.x > 0:
            player_1.x -= 1
        elif keyboard[pygame.K_RIGHT] and player_1.x < WIDTH:
            player_1.x += 1
        elif keyboard[pygame.K_UP] and player_1.y > 0:
            player_1.y -= 1
        elif keyboard[pygame.K_DOWN] and player_1.y < HEIGHT:
            player_1.y += 1
    if keyboard[pygame.K_LEFT]:
        dx -= 1
    if keyboard[pygame.K_RIGHT]:
        dx += 1
    if keyboard[pygame.K_UP]:
        dy -= 1
    if keyboard[pygame.K_DOWN]:
        dy += 1
    if keyboard[pygame.K_w]:
        wy -= 1
    if keyboard[pygame.K_s]:
        wy += 1
    if keyboard[pygame.K_a]:
        wx -= 1
    if keyboard[pygame.K_d]:
        wx += 1

    # username_screen = font.render(username, True, RED)
    # screen.blit(username_screen, (player_1.x, player_1.y + 50))
    update()

    player_1.move_player(dx, dy)
    hunter_1.move_player(wx, wy)
    pygame.display.update()
    clock.tick(30)

# print(username)
pygame.quit()
sys.exit()





