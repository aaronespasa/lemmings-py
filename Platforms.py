"""
Create the platforms and the gates of the game.
"""
import pyxel
from random import randint

from Gameboard import Gameboard

class Platforms:
    def __init__(self):
        self.gameboard = Gameboard()

        # DIMENSIONS
        self.width = self.gameboard.width
        self.height = self.gameboard.height
        self.cell_size = self.gameboard.cell_size

        # GAMEBOARD VALUES
        self.grid_rows = self.gameboard.grid_rows
        self.grid_columns = self.gameboard.grid_columns
        self.scoreboard = self.gameboard.scoreboard

        # PLATFORMS
        self.platform_minimum_size = 5
        self.platform_maximum_size = 10
        self.platforms_num = 7
        self.platforms = self.generate_platforms(
                            self.platform_minimum_size,
                            self.platform_maximum_size,
                            self.platforms_num
                        )
        
        # GATES
        self.entry_gate = self.generate_gate(self.platforms, self.platforms_num)
        self.exit_gate = self.generate_gate(
                              self.platforms, self.platforms_num, exit_gate=True)

    def generate_platforms(self, min_size, max_size, platforms_num):
        """Create the platforms
        :param min_size (int): Minimum size (num of the cells) of the platform
        :param max_size (int): Maximum size (num of the cells) of the platform
        :param platforms_num (int): Num of platforms that have to be displayed
        :return list: List with platforms_num dicts that have the x and y coordinates,
        the width and the height of the platform
        """
        platforms_schema = {
            "x": 0,
            "y": 0,
            "width": 0,
            "height": self.cell_size,
            "position": ""
        }
        platforms = []
        
        # Platform at the bottom
        platforms.append({
            "x": 0,
            "y": 224,
            "width": self.width,
            "height": self.cell_size,
            "position": "right"
        })

        row_coordinates = [0]
        # The platform will be on the left or right
        position = ["right", "left"]

        for i in range(platforms_num):
            platforms.append(platforms_schema.copy())
            platform_row = 0
            # platform_row cannot be repeated to avoid overlapping
            while platform_row in row_coordinates:
                # self.grid_rows - 1 prevents the program from
                # putting a row underneath the platform at the bottom

                platform_row = randint(1, self.grid_rows - 2)
            row_coordinates.append(platform_row)

            platforms[i]["position"] = position[randint(0, 1)]
            platforms[i]["width"] = (randint(min_size, max_size)
                                     * self.cell_size)

            if platforms[i]["position"] == "left":
               platforms[i]["x"] = 0
            elif platforms[i]["position"] == "right":
                platforms[i]["x"] = ((self.grid_columns * self.cell_size) -
                                     platforms[i]["width"])
            
            platforms[i]["y"] = (platform_row * self.cell_size
                                 + self.scoreboard["height"])

        return platforms

    def generate_gate(self, platforms, platforms_num, exit_gate=False):
        """Create a gate
        :param platforms (list): List containing self.platforms_num elements
                                 with the following form: [platform_row, platform_size]
        :param exit_gate (bool): True if the gate is the exit_gate
        :return dict: Dict containing the x and y values of the gate
        """
        gate = {
            "x": 0,
            "y": 0
        }
        row_index = randint(0, platforms_num - 1)

        if exit_gate == True:
            # Prevent the two gates from being in the same row
            while row_index == (self.entry_gate["y"] / self.cell_size):
                row_index = randint(0, platforms_num - 1)
        
        # We multiply by self.cell_size to get the "coordinates"
        gate["y"] = platforms[row_index]["y"]

        # Set the x of the gate between the beginning of the platform
        # and the final of it: randint(beginning, final)
        if platforms[row_index]["position"] == "left":
            gate["x"] = randint(1, platforms[row_index]["width"])
        elif platforms[row_index]["position"] == "right":
            x_i = self.width - platforms[row_index]["width"]
            gate["x"] = randint(x_i, self.width)

        return gate
