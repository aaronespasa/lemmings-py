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
        self.game_over = [False, ""]

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
            # Start the game
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

            idx, is_tool = self.same_tool_there(umbrella_x, umbrella_y, self.tools["umbrella"])

            if is_tool:
                # check if there's the same umbrella already there
                self.tools["umbrella"].pop(idx)
            elif not self.tool_in_tools(umbrella_x, umbrella_y):
                self.tools["umbrella"].append([umbrella_x, umbrella_y, umbrella_img])

        elif pyxel.btnp(pyxel.KEY_B):
            # Place a blocker
            tools = Tools(self.user_x, self.user_y, "blocker")
            blocker_x, blocker_y, blocker_img = tools.blocker()
            
            idx, is_tool = self.same_tool_there(blocker_x, blocker_y, self.tools["blocker"])

            if is_tool:
                # check if there's the same blocker already there
                self.tools["blocker"].pop(idx)
            elif not self.tool_in_tools(blocker_x, blocker_y):
                self.tools["blocker"].append([blocker_x, blocker_y, blocker_img])
        elif pyxel.btnp(pyxel.KEY_R):
            # Place a right stair
            tools = Tools(self.user_x, self.user_y, "right_stair")
            right_s_x, right_s_y, right_s_right, right_s_img = tools.right_stair()
            
            if not self.tool_in_tools(right_s_x, right_s_y):
                self.tools["right_s"].append([right_s_x, right_s_y, right_s_right, right_s_img])
        elif pyxel.btnp(pyxel.KEY_L):
            # Place a left stair
            tools = Tools(self.user_x, self.user_y, "left_stair")
            left_s_x, left_s_y, left_s_left, left_s_img = tools.left_stair()

            if not self.tool_in_tools(left_s_x, left_s_y):
                self.tools["left_s"].append([left_s_x, left_s_y, left_s_left, left_s_img])
        elif pyxel.btnp(pyxel.KEY_Q):
            # Quit the program
            pyxel.quit()
    
    def tool_in_tools(self, tool_x, tool_y):
        """Check if the coordinates x and y of the tools coincide
        with some existing ones of any tool"""        
        for umbrella in self.tools["umbrella"]:
            # Check if it coincides with an umbrella
            if umbrella[0] == tool_x and umbrella[1] == tool_y:
                return True
        for blocker in self.tools["blocker"]:
            # Check if it coincides with a blocker
            if blocker[0] == tool_x and blocker[1] == tool_y:
                return True
        for right_s in self.tools["right_s"]:
            # Check if it coincides with a right stair
            if right_s[0] == tool_x and right_s[1] == tool_y:
                return True
        for left_s in self.tools["left_s"]:
            # Check if it coincides with a left stair
            if left_s[0] == tool_x and left_s[1] == tool_y:
                return True
        return False
    
    def same_tool_there(self, tool_x, tool_y, tool_list):
        """The same tool is there"""
        is_tool = False
        idx = 0
        for i in range(len(tool_list)):
            if tool_x == tool_list[i][0] and tool_y == tool_list[i][1]:
                is_tool = True
                idx = i

        return idx, is_tool


    def update(self):
        """Updates the players and draw the game."""
        # LEMMINGS
        if self.start and not self.game_over[0]:
            lemmings = self.Lemming.update_player(self.tools)
        
            for i in range(len(lemmings)):
                if (lemmings[i].x == self.exit_gate.x and
                    lemmings[i].y == self.exit_gate.y and
                    i not in self.saved):
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
        
        if len(self.saved) == self.lemmings_num:
            self.game_over[0] = True
            self.game_over[1] = "win"
        elif len(self.dead) == self.lemmings_num:
            self.game_over[0] = True
            self.game_over[1] = "lose"
            
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
        if self.start and self.game_over[0]:
            self.Draw.draw_game(self.scoreboard, self.Lemming.before_start(),
                                self.user_x, self.user_y, self.tools, self.start, self.game_over[1])
        elif self.start:
            self.Draw.draw_game(self.scoreboard, lemmings,
                                self.user_x, self.user_y, self.tools, self.start)
        else:
            self.Draw.draw_game(self.scoreboard, self.Lemming.before_start(),
                                self.user_x, self.user_y, self.tools, self.start)

App()
