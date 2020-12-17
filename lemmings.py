"""Main program"""
import pyxel
import time
from Player import Player
from Platforms import Platforms # Platforms and gates
from Gameboard import Gameboard # Matrix
from Draw import Draw # Visual
from Tools import Tools

class Lemming:
    def __init__(self):
        # TIME
        self.initial_time = time.time()
        self.click_time = self.initial_time
        self.click_delay = 0.5 # s

        # DIMENSIONS
        self.Gameboard = Gameboard()
        self.width = self.Gameboard.width
        self.height = self.Gameboard.height
        self.cell_size = self.Gameboard.cell_size

        # TOOLS
        self.grid = self.Gameboard.grid
        self.Tools = Tools(self.grid, self.cell_size)

        # PLATFORMS AND GATES
        self.Platforms = Platforms()
        self.platforms = self.Platforms.platforms
        self.entry_gate = self.Platforms.entry_gate
        self.exit_gate = self.Platforms.exit_gate

        self.Player = Player(self.entry_gate, self.exit_gate, self.platforms, self.width)
        
        # DRAW
        self.Draw = Draw(self.platforms, self.entry_gate,
                         self.exit_gate)

        self.pyxel_window_title = "Lemmings"
        pyxel.init(self.width, self.height, caption=self.pyxel_window_title)
        pyxel.run(self.exit_option, self.update)

    def exit_option(self):
        """Quit the program by pressing Q"""
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def update(self):
        """Update the time, score"""
        level = 0
        alive = 0
        saved = 0
        died = 0
        ladders = 0
        umbrellas = 0
        blockers = 0

        current_time = time.time()
        
        players = self.Player.update_player()
        
        pyxel.mouse(True)
        
        delay_condition = (time.time() - self.click_time) > self.click_delay
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and delay_condition:
            square, selected_tool = self.Tools.tool(pyxel.mouse_x, pyxel.mouse_y)
            
            self.click_time = time.time()
            
            self.Draw.draw_game(level, alive, saved, died, ladders,
                                umbrellas, blockers, players, square,
                                selected_tool)
        else:
            self.Draw.draw_game(level, alive, saved, died, ladders,
                                umbrellas, blockers, players)

Lemming()
