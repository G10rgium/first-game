from select import select


class Player:
    def __init__(self):
        self.size = 50
        self.x = 30
        self.y = 30
        self.speed = 5

    def move_player(self, x_position, y_position):
        # dx = x_position - self.x
        # dy = y_position - self.y
        self.x += x_position * self.speed
        self.y += y_position * self.speed


