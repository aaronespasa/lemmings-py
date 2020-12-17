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
            "x_i": 0,
            "x": 0,
            "start": True,
            "y": self.entry_gate["y"],
            "width": 5,
            "height": 5,
            "alive": True,
            "movement": 0,
            "direction": "right"
        }

        players_num = randint(10, 20)
        
        for i in range(players_num):
            players.append(player_stats)
            # Create a distance of i / 2 between the lemmings
            players[i]["x_i"] = self.entry_gate["x"]

        return players

    def update_player(self):
        """Move autonomously"""
        for i in range(len(self.players)):

            if self.players[i]["x"] == self.width - self.players[i]["width"] - 1:
                # Player at the right of the window
                self.players[i]["direction"] = "left"
                self.players[i]["start"] = False
                self.players[i]["movement"] = 0
            elif self.players[i]["x"] == 0:
                # Player at the left of the window
                self.players[i]["direction"] = "right"
                # self.players[i]["movement"] = 0
            
            # Increase the movement in the correct direction
            if self.players[i]["direction"] == "right":
            
                if self.players[i]["start"] == True:
                    # Make the movement range of the player between the width
                    # and its initial position (the player has started the game)
                    movement_range = self.width - self.players[i]["x_i"] - self.players[i]["width"]
                    
                    self.players[i]["movement"] = (pyxel.frame_count) % movement_range
                    
                    self.players[i]["x"] = self.players[i]["x_i"] + self.players[i]["movement"]
                else:
                    # Make the movement range of the player all the width
                    # (the player is at the left of the window)
                    movement_range = self.width - self.players[i]["width"]
                    
                    self.players[i]["movement"] = (pyxel.frame_count) % movement_range

                    self.players[i]["x"] = self.players[i]["movement"]
                
                # print(f"right movement: {self.players[i]['movement']}")
                
                self.players[i]["x_f"] = self.players[i]["movement"]
                
            elif self.players[i]["direction"] == "left":
                movement_range = self.width - self.players[i]["width"]
                
                self.players[i]["movement"] = (- pyxel.frame_count) % self.width

                self.players[i]["x"] = self.players[i]["x_f"] + self.players[i]["movement"]
                
                # print(f"left movement: {self.players[i]['movement']}")

            #     self.players[i]["movement"] = - (pyxel.frame_count) % (movement_range)
                
            #     # Update the x
            #     self.players[i]["x"] = self.players[i]["movement"] - \
            #         (self.players[i]["x_f"])
                
        
        return self.players

    def remove_player(self):
        """Remove player if it dies.
        It can die if:
        - Falls more than three squares of the map grid
        - Is touched by a saw
        - The player replay the game
        """
        pass
