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
        self.start = False

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
        self.entry_gate= self.Gameboard.generate_gate(self.platforms)
        self.exit_gate = self.Gameboard.generate_gate(self.platforms,
                                    self.entry_gate.row_index, exit_gate=True)

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
        self.alive = []
        self.saved = []
        self.dead = []
        self.Lemming = Lemming(self.entry_gate.x, self.entry_gate.y, self.platforms)
        self.lemmings_num = self.Lemming.lemmings_num
        
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
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.start = True
        elif pyxel.btnp(pyxel.KEY_LEFT) and self.user_x > 0:
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
        if self.start == True:
            lemmings = self.Lemming.update_player(self.tools)
        
            for i in range(len(lemmings)):
                if lemmings[i].saved and i not in self.saved:
                    # Lemming saved
                    self.saved.append(i)
                    if i in self.alive:
                        self.alive.remove(i)
                    
                elif lemmings[i].alive and i not in self.alive:
                    # Lemming alive
                    self.alive.append(i)
                elif lemmings[i].alive == False and i not in self.dead:
                    # Lemming dead
                    self.dead.append(i)
                    if i in self.alive:
                        self.alive.remove(i)
            
        # SCOREBOARD
        total_alive = len(self.alive)
        total_saved = len(self.saved)
        total_dead = len(self.dead)
        total_stairs = len(self.tools["right_s"]) + len(self.tools["left_s"])
        total_umbrellas = len(self.tools["umbrella"])
        total_blockers = len(self.tools["blocker"])
        self.scoreboard = Scoreboard(self.level, total_alive, total_saved, total_dead,
                                     total_stairs, total_umbrellas, total_blockers)

        # DRAW
        if self.start:
            self.Draw.draw_game(self.scoreboard, lemmings,
                                self.user_x, self.user_y, self.tools, self.start)
        else:
            self.Draw.draw_game(self.scoreboard, self.Lemming.before_start(),
                                self.user_x, self.user_y, self.tools, self.start)

App()
