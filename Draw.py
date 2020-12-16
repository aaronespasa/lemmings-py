"""
Display all the visuals of the game.
"""
import pyxel
from Gameboard import Gameboard

class Draw:
    def __init__(self, platforms, entry_gate, exit_gate):
        self.gameboard = Gameboard()

        # DIMENSIONS
        self.width = self.gameboard.width
        self.height = self.gameboard.height
        self.cell_size = self.gameboard.cell_size
        self.grid_columns = self.gameboard.grid_columns

        # COLORS
        self.BLACK = 0
        self.DARK_BLUE = 1
        self.BROWN = 4
        self.WHITE = 7
        self.GREEN = 11
        self.BLUE = 12

        # MAIN OBJECTS
        self.platforms = platforms
        self.entry_gate = entry_gate
        self.exit_gate = exit_gate
        self.scoreboard = self.gameboard.scoreboard
        # self.grid = self.gameboard.grid

    def draw_game(self, level, alive, saved, died, ladders,
                  umbrellas, blockers):
        """Display the map of the game including:
        - The scoreboard
        - The platform
        """
        pyxel.cls(self.BLUE)

        # Display the scoreboard
        pyxel.rect(self.scoreboard["x"], self.scoreboard["y"],
                   self.scoreboard["width"], self.scoreboard["height"],
                   self.scoreboard["bgcolor"])

        first_row_height = self.scoreboard["height"] / 4
        second_row_height = self.scoreboard["height"] / 1.5

        self.scoreboard["level"] = f"Level: {level}"
        pyxel.text(5, first_row_height,
                   self.scoreboard["level"], self.scoreboard["textcolor"])

        self.scoreboard["alive"] = f"Alive: {alive}"
        pyxel.text(self.scoreboard["width"] / 4, first_row_height,
                   self.scoreboard["alive"], self.scoreboard["textcolor"])
        
        self.scoreboard["saved"] = f"Saved: {saved}"
        pyxel.text(self.scoreboard["width"] / 2, first_row_height,
                   self.scoreboard["saved"], self.scoreboard["textcolor"])

        self.scoreboard["died"] = f"Died: {died}"
        pyxel.text(self.scoreboard["width"] - 60, first_row_height,
                   self.scoreboard["died"], self.scoreboard["textcolor"])

        self.scoreboard["ladders"] = f"Ladders: {ladders}"
        pyxel.text(5, second_row_height,
                   self.scoreboard["ladders"], self.scoreboard["textcolor"])

        self.scoreboard["umbrellas"] = f"Umbrellas: {umbrellas}"
        pyxel.text(self.scoreboard["width"] / 2 - 40, second_row_height,
                   self.scoreboard["umbrellas"], self.scoreboard["textcolor"])

        self.scoreboard["blockers"] = f"Blockers: {blockers}"
        pyxel.text(self.scoreboard["width"] / 2 + 48, second_row_height,
                   self.scoreboard["umbrellas"], self.scoreboard["textcolor"])

        # # Display the grid of the game
        # for cell_num in range(len(self.grid)):
        #     pyxel.rectb(self.grid[cell_num][0], self.grid[cell_num][1],
        #                 self.cell_size, self.cell_size, self.WHITE)

        # Display the platform
        for i in range(len(self.platforms)):
            # Soil
            pyxel.rect(self.platforms[i]["x"], self.platforms[i]["y"],
                       self.platforms[i]["width"], self.platforms[i]["height"], self.BROWN)
            # Grass
            grass_size = 3
            pyxel.rect(self.platforms[i]["x"], self.platforms[i]["y"],
                       self.platforms[i]["width"], grass_size, self.GREEN)
        
        # Display the gates
        pyxel.rectb(self.entry_gate["x"], self.entry_gate["y"],
                    5, 3, self.WHITE)
        pyxel.rectb(self.exit_gate["x"], self.exit_gate["y"],
                    5, 3, self.BLACK)
