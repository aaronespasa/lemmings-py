"""
Player class.
"""
from time import time

class Player:
    def __init__(self, x: int, y: int, direction: str = "right"):
        self.x_i = x
        self.x = x
        self.x_f = x
        self.y_before_falling = y
        self.y = y
        self.direction = direction
        self.alive = True
        self.movement = 0
        self.falling = False
        self.speed = 30  # Default speed

        # This times will be updated when the lemming
        # reaches a platform after falling
        self.player_time_x = time()
        self.player_time_y = time()

        self.height = 5
        self.width = 5

        self.start = True
        self.img = (0, 32, 16, 16, 16, 0)
