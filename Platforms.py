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
        self.cell_size = self.gameboard.cell_size
        self.scoreboard = self.gameboard.scoreboard

        # COLORS
        self.black = 0
        self.white = 7
        self.dark_blue = 1

        self.pyxel_window_title = "Lemmings"
        pyxel.init(self.width, self.height, caption=self.pyxel_window_title)
        pyxel.run(self.exit_option, self.draw_game)

    def exit_option(self):
        """Quit the program by pressing Q"""
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw_game(self):
        pyxel.cls(self.black)

        # Gameboard example
        for cell_num in range(len(self.grid)):
            # Display the scoreboard
            pyxel.rect(self.scoreboard["x"], self.scoreboard["y"],
                       self.scoreboard["width"], self.scoreboard["height"],
                       self.scoreboard["bgcolor"])

            text_box_size = 18
            pyxel.text(self.scoreboard["width"] / 2 - text_box_size, self.scoreboard["height"] / 2,
                       self.scoreboard["text"], self.scoreboard["textcolor"])

            # Display the grid of the game
            pyxel.rectb(self.grid[cell_num][0], self.grid[cell_num][1],
                        self.cell_size, self.cell_size, self.white)
