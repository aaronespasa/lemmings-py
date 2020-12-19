"""Main program"""
import pyxel
from time import time
from Lemming import Lemming # Players
# Grid, Gates and Platforms
from Gameboard import Gameboard
from Draw import Draw # Visual
from Tools import Tools
from Scoreboard import Scoreboard

class App:
    def __init__(self):
        # TIME
        self.initial_time = time()

        # GAMEBOARD
        self.Gameboard = Gameboard()
        self.constants = self.Gameboard.Constants
        self.width = self.constants.width
        self.height = self.constants.height
        self.cell_size = self.constants.cell_size
        self.grid = self.Gameboard.grid

        # SCOREBOARD
        self.scoreboard = Scoreboard()

        # TOOLS
        self.user_x = 0
        self.user_y = 32
        self.cursor_displacement = 16
        self.Tools = Tools(self.grid, self.cell_size)

        # PLATFORMS AND GATES
        self.platforms = self.Gameboard.platforms
        self.entry_gate = self.Gameboard.entry_gate
        self.exit_gate = self.Gameboard.exit_gate

        self.Lemming = Lemming(self.entry_gate.x, self.entry_gate.y, self.platforms)
        
        # DRAW
        self.Draw = Draw(self.platforms, self.entry_gate,
                         self.exit_gate)

        self.pyxel_window_title = "Lemmings"
        pyxel.init(self.Gameboard.Constants.width,
                   self.Gameboard.Constants.height,
                   caption=self.pyxel_window_title)
        pyxel.load("./assets/resources.pyxres")
        pyxel.run(self.update, self.interaction)

    def update(self):
        """Update the time, score"""

        current_time = time()
        
        lemmings = self.Lemming.update_player()

        # Update scoreboard

        self.Draw.draw_game(self.scoreboard, lemmings, self.user_x, self.user_y)
    
    def interaction(self):
        """Allows the user to interact with the grid to place tools in the map.
        This function also add the option to quit the program by pressing Q.
        """
        if pyxel.btnp(pyxel.KEY_LEFT) and self.user_x > 0:
            self.user_x -= self.cursor_displacement
        elif pyxel.btnp(pyxel.KEY_RIGHT) and self.user_x < self.width - 16:
            self.user_x += self.cursor_displacement
        elif pyxel.btnp(pyxel.KEY_UP) and self.user_y > 32:
            self.user_y -= self.cursor_displacement
        elif pyxel.btnp(pyxel.KEY_DOWN) and self.user_y < self.height - 16:
            self.user_y += self.cursor_displacement
        elif pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        
App()
