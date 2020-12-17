from random import randint
import pyxel

class Player:
    def __init__(self, entry_gate, exit_gate, platforms, width):
        self.entry_gate = entry_gate
        self.exit_gate = exit_gate
        self.platforms = platforms
        self.width = width
        self.players = self.create_players()
        

    def create_players(self):
        """Create a number of players between 10 and 20
        and assign to each one of them the coordinates x and y
        and also if the player is alive."""
        players = []

        player_stats = {
            "x": 0,
            "y": self.entry_gate["y"],
            "alive": True,
            "movement": 0,
            "direction": "right"
        }

        players_num = randint(10, 20)
        
        for i in range(players_num):
            players.append(player_stats)
            # Create a distance of i / 2 between the lemmings
            players[i]["x"] = self.entry_gate["x"]
        
        return players

    def update_player(self):
        """Move autonomously"""
        for i in range(len(self.players)):
            x = self.players[i]["x"] + self.players[i]["movement"]
            print(x)
            if x == self.width - 1:
                # Player at the right of the window
                self.players[i]["direction"] = "left"
                self.players[i]["movement"] = 0
            elif x == 0:
                # Player at the left of the window
                self.players[i]["direction"] = "right"
                self.players[i]["movement"] = 0
            
            # Increase the movement in the correct direction
            if self.players[i]["direction"] == "right":
                self.players[i]["movement"] = pyxel.frame_count % (
                    self.width - self.players[i]["x"])
            elif self.players[i]["direction"] == "left":
                self.players[i]["movement"] = - pyxel.frame_count % (
                    self.width)
        
        return self.players

    def remove_player(self):
        """Remove player if it dies.
        It can die if:
        - Falls more than three squares of the map grid
        - Is touched by a saw
        - The player replay the game
        """
        pass
