"""Main program"""
import pyxel
import time
from Player import Player
from Platforms import Platforms # Platforms and gates
from Gameboard import Gameboard # Matrix
from Draw import Draw # Visual

class Lemming:
    def __init__(self):
        # time: int
        # tools: upper stairs, down stairs, umbrella, blocker    

        # DIMENSIONS
        self.Gameboard = Gameboard()
        self.width = self.Gameboard.width
        self.height = self.Gameboard.height

        # PLATFORMS AND GATES
        self.Platforms = Platforms()
        self.platforms = self.Platforms.platforms
        self.entry_gate = self.Platforms.entry_gate
        self.exit_gate = self.Platforms.exit_gate

        Player(self.entry_gate, self.exit_gate)
        
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
        self.Draw.draw_game(level, alive, saved, died, ladders,
                            umbrellas, blockers)

Lemming()
