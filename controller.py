from select import select

from random import randint

class Player:
    def __init__(self):
        self.size = 80
        self.x = 960
        self.y = 540
        self.speed = 5

    def move_player(self, x_position, y_position):
        # dx = x_position - self.x
        # dy = y_position - self.y
        self.x += x_position * self.speed
        self.y += y_position * self.speed


class Bamboo:
    def __init__(self):
        self.size = 50
        self.x = randint(0, 1920)
        self.y = randint(0, 1080)


class Player2:
    def __init__(self):
        self.size = 80
        self.x = 560
        self.y = 240
        self.speed = 5
    def move_player(self, x_position, y_position):
        self.x += x_position * self.speed
        self.y += y_position * self.speed


