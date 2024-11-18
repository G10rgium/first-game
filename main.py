import sys
from idlelib.replace import replace
from os import remove

import pygame

from random import randint

# class Player:
#     def __init__(self):
#         self.size = 80
#         self.x = 960
#         self.y = 540
#         self.speed = 5
#
#     def move_player(self, x_position, y_position):
#         # dx = x_position - self.x
#         # dy = y_position - self.y
#         self.x += x_position * self.speed
#         self.y += y_position * self.speed
#
#
# class Bamboo:
#     def __init__(self):
#         self.size = 50
#         self.x = randint(0, 1920)
#         self.y = randint(0, 1080)
#
#
# class Player2:
#     def __init__(self):
#         self.size = 80
#         self.x = 560
#         self.y = 240
#         self.speed = 5
#     def move_player(self, x_position, y_position):
#         self.x += x_position * self.speed
#         self.y += y_position * self.speed

pygame.init()

background_image = pygame.image.load("background_1.png")

player_image = pygame.image.load("panda-bear.png")

hunter = pygame.image.load("lumberjack.png")

hunter_1 = pygame.Rect(randint(0, 1820), randint(0, 1000), 80, 80)

WIDTH = 1920
HEIGHT = 1080

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_1 = pygame.Rect(randint(0, 1820), randint(0, 1000), 80, 80)

size = 80, 80

pygame.display.set_caption("user: ")

font = pygame.font.SysFont('Arial', 30)

bamboo = pygame.image.load("bamboo.png")

vel_panda = 12

vel_hunter = 10

bambo = pygame.Rect(randint(0, 1820), randint(0, 1000), 80, 80)
size_1 = pygame.transform.scale(player_image, size)
size_2 = pygame.transform.scale(hunter, size)
size_3 = pygame.transform.scale(bamboo, size)

L_wall = pygame.Rect(0, 0, 1, HEIGHT)
R_wall = pygame.Rect(WIDTH, 0, 1, HEIGHT)
T_wall = pygame.Rect(0, 0, WIDTH, 1)
B_wall = pygame.Rect(0, HEIGHT, WIDTH, 1)

score = 0

running = True
while running:
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





        # if event.type == pygame.KEYDOWN:
        #     username += event.unicode
    # pygame.draw.rect(screen, BLACk, (player_1.x, player_1.y, player_1.size, player_1.size))
    screen.blit(size_1, player_1)
    screen.blit(size_3, bambo)
    screen.blit(size_2, hunter_1)

    # print(keyboard)
    # dx = 0
    # dy = 0
    # wx = 0
    # wy = 0
    # def update():
    #     if keyboard[pygame.K_LEFT] and player_1.x > 0:
    #         player_1.x -= 1
    #     elif keyboard[pygame.K_RIGHT] and player_1.x < WIDTH:
    #         player_1.x += 1
    #     elif keyboard[pygame.K_UP] and player_1.y > 0:
    #         player_1.y -= 1
    #     elif keyboard[pygame.K_DOWN] and player_1.y < HEIGHT:
    #         player_1.y += 1
    keyboard = pygame.key.get_pressed()
    if keyboard[pygame.K_LEFT]:
        player_1.x -= vel_panda
    if keyboard[pygame.K_RIGHT]:
        player_1.x += vel_panda
    if keyboard[pygame.K_UP]:
        player_1.y -= vel_panda
    if keyboard[pygame.K_DOWN]:
        player_1.y += vel_panda
    if keyboard[pygame.K_w]:
        hunter_1.y -= vel_hunter
    if keyboard[pygame.K_s]:
        hunter_1.y += vel_hunter
    if keyboard[pygame.K_a]:
        hunter_1.x -= vel_hunter
    if keyboard[pygame.K_d]:
        hunter_1.x += vel_hunter

    username_screen = font.render("SCORE: " + str(score), False, RED)
    screen.blit(username_screen, (960, 0))
    # update()

    if player_1.colliderect(hunter_1):
        pygame.draw.rect(screen, (255, 0, 0), player_1, 4)

    if player_1.colliderect(bambo):
        bambo = pygame.Rect(randint(0, 1820), randint(0, 1000), 80, 80)
        score += 1

    if player_1.colliderect(L_wall):
        player_1.x = 0
    if player_1.colliderect(R_wall):
        player_1.x = 0
    if player_1.colliderect(T_wall):
        player_1.y = 0
    if player_1.colliderect(B_wall):
        player_1.y = 0


    pygame.display.update()
    clock.tick(30)

# print(username)
pygame.quit()
sys.exit()






