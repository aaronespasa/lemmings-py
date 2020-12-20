"""
Player class.
"""
from time import time

class Player:
    def __init__(self, x: int, y: int, direction: str = "right"):
        # self.x_i = x
        self.x = x
        # self.x_f = x
        # self.y_before_falling = y
        self.y = y
        self.direction = direction
        self.alive = True
        # self.movement = 0
        self.falling = False
        self.speed = 1  # Default speed (1px)

        # This times will be updated when the lemming
        # reaches a platform after falling
        # self.time_x_bef_falling = 0.0
        # self.time_x_falling = 0.0
        # self.player_time_x = time()
        # self.player_time_y = time()

        # self.start = True
        self.img = (0, 32, 16, 16, 16, 0)
