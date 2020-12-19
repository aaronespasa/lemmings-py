"""
Create the platforms and the gates of the game.
"""
import pyxel
from random import randint

from .Constants import Constants

class Platforms:
    def __init__(self):
        self.constants = Constants()
        
        # DIMENSIONS
        self.width = self.constants.width
        self.height = self.constants.cell_size
        self.cell_size = self.constants.cell_size

        # GRID VALUES
        self.grid_rows = self.constants.grid_rows
        self.grid_columns = self.constants.grid_columns

        # PLATFORMS
        self.platform_min_size = self.constants.platform_min_size
        self.platform_max_size = self.constants.platform_max_size
        self.platforms_num = self.constants.platforms_num

        self.img = (0, 48, 16, 16, 16, 0)
