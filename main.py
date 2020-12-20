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
        # GAME: MAIN VARIABLES
        self.initial_time = time()
        self.level = 0

        # GAMEBOARD
        self.Gameboard = Gameboard()
        self.constants = self.Gameboard.Constants
        self.width = self.constants.width
        self.height = self.constants.height
        self.cell_size = self.constants.cell_size
        self.grid = self.Gameboard.grid

        # SCOREBOARD
        self.scoreboard = Scoreboard()

        # PLATFORMS AND GATES
        self.platforms = self.Gameboard.platforms
        self.entry_gate = self.Gameboard.entry_gate
        self.exit_gate = self.Gameboard.exit_gate

        # TOOLS
        self.user_x = 0
        self.user_y = self.scoreboard.height
        self.cursor_displacement = self.cell_size
        self.tools = {
            "umbrella": [],
            "blocker": [],
            "right_s": [],
            "left_s": []
        }

        # LEMMING
        self.alive = 0
        self.saved = 0
        self.died = 0
        self.Lemming = Lemming(self.entry_gate.x, self.entry_gate.y, self.platforms)
        
        # DRAW
        self.Draw = Draw(self.platforms, self.entry_gate,
                         self.exit_gate)

        # PYXEL
        self.pyxel_window_title = "Lemmings"
        pyxel.init(self.width, self.height, caption=self.pyxel_window_title)

        pyxel.load("./assets/resources.pyxres")

        pyxel.run(self.interaction, self.update)
    
    def interaction(self):
        """Allows the user to interact with the grid to place tools in the map.
        This function also add the option to quit the program by pressing Q.
        """
        if pyxel.btnp(pyxel.KEY_LEFT) and self.user_x > 0:
            # Move to the left
            self.user_x -= self.cursor_displacement
        elif pyxel.btnp(pyxel.KEY_RIGHT) and self.user_x < self.width - 16:
            # Move to the right
            self.user_x += self.cursor_displacement
        elif pyxel.btnp(pyxel.KEY_UP) and self.user_y > 32:
            # Move up
            self.user_y -= self.cursor_displacement
        elif pyxel.btnp(pyxel.KEY_DOWN) and self.user_y < self.height - 16:
            # Move down
            self.user_y += self.cursor_displacement
        elif pyxel.btnp(pyxel.KEY_U):
            # Place an umbrella
            tools = Tools(self.user_x, self.user_y, "umbrella")
            umbrella_x, umbrella_y, umbrella_img = tools.umbrella()
            self.tools["umbrella"].append([umbrella_x, umbrella_y, umbrella_img])
        elif pyxel.btnp(pyxel.KEY_B):
            # Place a blocker
            tools = Tools(self.user_x, self.user_y, "blocker")
            blocker_x, blocker_y, blocker_img = tools.blocker()
            self.tools["blocker"].append([blocker_x, blocker_y, blocker_img])
        elif pyxel.btnp(pyxel.KEY_R):
            # Place a right stair
            tools = Tools(self.user_x, self.user_y, "right_stair")
            right_s_x, right_s_y, right_s_right, right_s_img = tools.right_stair()
            self.tools["right_s"].append([right_s_x, right_s_y, right_s_right, right_s_img])
        elif pyxel.btnp(pyxel.KEY_L):
            # Place a left stair
            tools = Tools(self.user_x, self.user_y, "left_stair")
            left_s_x, left_s_y, left_s_left, left_s_img = tools.left_stair()
            self.tools["left_s"].append([left_s_x, left_s_y, left_s_left, left_s_img])
        elif pyxel.btnp(pyxel.KEY_Q):
            # Quit the program
            pyxel.quit()
    
    def update(self):
        """Updates the players and draw the game."""
        # LEMMINGS
        lemmings = self.Lemming.update_player()

        # SCOREBOARD
        total_stairs = len(self.tools["right_s"]) + len(self.tools["left_s"])
        total_umbrellas = len(self.tools["umbrella"])
        total_blockers = len(self.tools["blocker"])
        self.scoreboard = Scoreboard(self.level, self.alive, self.saved, self.died,
                                     total_stairs, total_umbrellas, total_blockers)

        # DRAW
        self.Draw.draw_game(self.scoreboard, lemmings,
                            self.user_x, self.user_y, self.tools)

App()
