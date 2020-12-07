"""
Given the grid and the scoreboard of Gameboard,
create the map of the game
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

        # GAMEBOARD VALUES
        self.grid = self.gameboard.grid
        self.grid_rows = self.gameboard.grid_rows
        self.grid_columns = self.gameboard.grid_columns
        self.cell_size = self.gameboard.cell_size
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
        self.entry_gate = self.generate_gate(self.platforms)
        self.exit_gate = self.generate_gate(self.platforms, exit_gate=True)

        # COLORS
        self.black = 0
        self.white = 7
        self.dark_blue = 1
        self.blue = 12
        self.brown = 4
        self.green = 11

        self.pyxel_window_title = "Lemmings"
        pyxel.init(self.width, self.height, caption=self.pyxel_window_title)
        pyxel.run(self.exit_option, self.draw_game)

    def exit_option(self):
        """Quit the program by pressing Q"""
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def generate_platforms(self, min_size, max_size, platforms_num):
        """Create the platforms
        :param min_size (int): Minimum size (num of the cells) of the platform
        :param max_size (int): Maximum size (num of the cells) of the platform
        :param platforms_num (int): Num of platforms that have to be displayed
        :return list: With self.platforms_num elements of the form [platform_row, platform_size, position]
        """
        platforms = []
        row_coordinates = [0]
        # The platform will be on the left or right
        position = ["right", "left"]

        for _ in range(platforms_num):
            platform_row = 0
            # platform_row cannot be repeated to avoid overlapping
            while platform_row in row_coordinates:
                platform_row = randint(1, self.grid_rows)
            
            platform_size = randint(min_size, max_size)
            pos = position[randint(0, 1)]

            platforms.append([platform_row, platform_size, pos])
        
        return platforms

    def generate_gate(self, platforms, exit_gate=False):
        """Create a gate
        :param platforms (list): List containing self.platforms_num elements
                                 with the following form: [platform_row, platform_size]
        :param exit_gate (bool): True if the gate is the exit_gate
        :return list: List containing the row and the column where the gate is [row, column].
        """
        # ENTRY GATE
        gate = []
        rand_platform_row = randint(0, 6) # index
        if exit_gate == True:
            # Prevent the two gates from being in the same row
            while rand_platform_row == self.entry_gate[1]:
                rand_platform_row = randint(1, 7)
        gate.append(platforms[rand_platform_row][0])

        # To select the column of the gate we have to first
        # know if the platform is at the left or at the right
        if platforms[rand_platform_row][2] == "left":
            # The column is going to be between the first column and
            # the column represented by the size of the platform
            col = randint(1, platforms[rand_platform_row][1])
        else: # right
            # The column is going to be between the beginning of the platform
            # ,that we obtain by substracting the total num of columns - the platform size,
            # and the total number of columns 
            col = randint(self.grid_columns - platforms[rand_platform_row][1],
                          self.grid_columns)
        gate.append(col)

        return gate

    def draw_game(self):
        pyxel.cls(self.blue)

        # Display the scoreboard
        pyxel.rect(self.scoreboard["x"], self.scoreboard["y"],
                   self.scoreboard["width"], self.scoreboard["height"],
                   self.scoreboard["bgcolor"])
        
        text_box_size = 18
        pyxel.text(self.scoreboard["width"] / 2 - text_box_size, self.scoreboard["height"] / 2,
                   self.scoreboard["text"], self.scoreboard["textcolor"])

        # # Display the grid of the game
        # for cell_num in range(len(self.grid)):
        #     pyxel.rectb(self.grid[cell_num][0], self.grid[cell_num][1],
        #                 self.cell_size, self.cell_size, self.white)

        # Display the platform
        for i in range(len(self.platforms)):
            platform_width = self.platforms[i][1] * self.cell_size
            platform_height = self.cell_size
            platform_row_coord = (self.platforms[i][0] * self.cell_size
                                  + self.scoreboard["height"])

            if self.platforms[i][2] == "left":
               platform_col_coord = 0 
            else: # right
                platform_col_coord = ((self.grid_columns * self.cell_size) -
                                     platform_width)
            # Soil
            pyxel.rect(platform_col_coord, platform_row_coord,
                      platform_width, platform_height, self.brown)
            # Grass
            grass_size = 3
            pyxel.rect(platform_col_coord, platform_row_coord,
                       platform_width, grass_size, self.green)
