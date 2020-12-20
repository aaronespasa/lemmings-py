"""
Display all the visuals of the game.
"""
import pyxel
from Gameboard import Gameboard

class Draw:
    def __init__(self, platforms, entry_gate, exit_gate):
        self.gameboard = Gameboard()
        self.constants = self.gameboard.Constants

        # DIMENSIONS
        self.width = self.constants.width
        self.height = self.constants.height
        self.cell_size = self.constants.cell_size
        self.grid_columns = self.constants.grid_columns

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
        # self.grid = self.gameboard.grid

    def draw_game(self, scoreboard, players, user_x, user_y, tools):
        """Display the map of the game including:
        - The scoreboard
        - The platform
        """
        pyxel.cls(5)

        # # GRID
        # for cell_num in range(len(self.grid)):
        #     pyxel.rectb(self.grid[cell_num][0], self.grid[cell_num][1],
        #                 self.cell_size, self.cell_size, self.WHITE)

        # SCOREBOARD
        scoreboard_text_color = 7 # Dark blue
        scoreboard_bg_color = 1 # white
        pyxel.rect(scoreboard.x, scoreboard.y,
                   scoreboard.width, scoreboard.height,
                   scoreboard_bg_color)

        first_row_height = scoreboard.height / 4
        second_row_height = scoreboard.height / 1.5

        pyxel.text(5, first_row_height,
                   scoreboard.level, scoreboard_text_color)

        pyxel.text(scoreboard.width / 4, first_row_height,
                   scoreboard.alive, scoreboard_text_color)
        
        pyxel.text(scoreboard.width / 2, first_row_height,
                   scoreboard.saved, scoreboard_text_color)

        pyxel.text(scoreboard.width - 60, first_row_height,
                   scoreboard.died, scoreboard_text_color)

        pyxel.text(5, second_row_height,
                   scoreboard.ladders, scoreboard_text_color)

        pyxel.text(scoreboard.width / 2 - 40, second_row_height,
                   scoreboard.umbrellas, scoreboard_text_color)

        pyxel.text(scoreboard.width / 2 + 52, second_row_height,
                   scoreboard.blockers, scoreboard_text_color)

        # PLATFORMS
        for platform in self.platforms:
            for i in range(int(platform.width / 16)):
                pyxel.blt(platform.x + i * 16, platform.y, *platform.img)
        
        # ENTRY GATE
        pyxel.blt(self.entry_gate.x, self.entry_gate.y - 
                  self.entry_gate.entry_img[4], *self.entry_gate.entry_img)
        # EXIT GATE
        pyxel.blt(self.exit_gate.x, self.exit_gate.y -
                  self.exit_gate.exit_img[4], *self.exit_gate.exit_img)
        
        # PLAYERS
        for player in players:
            pyxel.blt(player.x, player.y - player.img[4], *player.img)
        
        # TOOLS
        tools_height = 242
        tools_color = self.WHITE
        
        # Menu
        pyxel.text(5, tools_height,
                   "U: Umbrella", tools_color)

        pyxel.text(self.width / 4, tools_height,
                   "B: Blocker", tools_color)

        pyxel.text(self.width / 2 - 6, tools_height,
                   "R: Right Stairs", tools_color)
        
        pyxel.text(self.width - 63, tools_height,
                   "L: Left Stairs", tools_color)

        pyxel.text(self.width / 2 - 40, tools_height + 8,
                   "Q: Quit the game", tools_color)
        
        # User cursor
        pyxel.rectb(user_x, user_y,
                    self.cell_size, self.cell_size, self.WHITE)
        
        # Umbrella
        if len(tools["umbrella"]) > 0:
            for umbrella in tools["umbrella"]:
                pyxel.blt(umbrella[0], umbrella[1], *umbrella[2])
        
        # Blocker
        if len(tools["blocker"]) > 0:
            for blocker in tools["blocker"]:
                pyxel.blt(blocker[0], blocker[1], *blocker[2])
        
        # Right stair
        if len(tools["right_s"]) > 0:
            for right_s in tools["right_s"]:
                pyxel.blt(right_s[0], right_s[1], *right_s[2])

        # Left stair
        if len(tools["left_s"]) > 0:
            for left_s in tools["left_s"]:
                pyxel.blt(left_s[0], left_s[1], *left_s[2])
