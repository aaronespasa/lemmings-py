"""
Player class.
We used the library time instead of pyxel.frame_count
because it gave us more flexibility to change the speed
"""
from random import randint
import pyxel
import time

class Player:
    def __init__(self, entry_gate, exit_gate, platforms, width):
        self.entry_gate = entry_gate
        self.exit_gate = exit_gate
        self.platforms = platforms
        self.width = width
        self.player_time = time.time()
        self.player_time_y = time.time()
        self.player_speed = 30
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
            "direction": "right",
            "falling": False
        }

        players_num = randint(10, 20)
        
        for i in range(players_num):
            players.append(player_stats)
            players[i]["x_i"] = self.entry_gate["x"]

        return players

    def update_player(self):
        """Move autonomously"""
        platform_y = 0
        for i in range(len(self.players)):
            self.players[i]["falling"], platform_y = self.is_falling(self.players[i])
            
            if self.players[i]["falling"]:
                # The player is falling
                self.players[i]["movement"] = (
                    time.time() - self.player_time_y) * self.player_speed

                print(self.players[i]["movement"])

                self.players[i]["y"] = platform_y - self.players[i]["movement"]
            else:
                # The playing is not falling
                self.x_move()
                self.player_time_y = time.time()
        
        return self.players

    def is_falling(self, player):
        platform_y = 0
        for platform in self.platforms:
            
            if player["y"] == platform["y"]:
                # Set the final x of the platform
                if platform["position"] == "right":
                    platform_x_f = self.width
                elif platform["position"] == "left":
                    platform_x_f = platform["x"] + platform["width"]

                player_in_platform = player["x"] >= platform["x"] and (
                    player["x"] <= platform_x_f)
                
                if player_in_platform:
                    return(False, platform_y)
        
        return(True, platform_y)


    def x_move(self):
        for i in range(len(self.players)):
            if self.players[i]["x"] > self.width - self.players[i]["width"]:
                # Player at the right of the window
                self.players[i]["direction"] = "left"
                self.players[i]["start"] = False
                self.player_time = time.time()

            elif self.players[i]["x"] < 0:
                # Player at the left of the window
                self.players[i]["direction"] = "right"
                self.player_time = time.time()
            
            # Increase the movement in the correct direction
            if self.players[i]["direction"] == "right":
                
                self.players[i]["movement"] = (
                    time.time() - self.player_time) * self.player_speed

                if self.players[i]["start"] == True:                    
                    self.players[i]["x"] = self.players[i]["x_i"] + self.players[i]["movement"]
                else:
                    self.players[i]["x"] = self.players[i]["movement"]

                # Get the final x of the player before changing its direction 
                self.players[i]["x_f"] = self.players[i]["x"]
                
                
            elif self.players[i]["direction"] == "left":
                # The + 1 allows us to avoid enter on a loop
                # because of the self.players[i]["x"] < 0 condition
                self.players[i]["movement"] = (
                    time.time() - self.player_time) * self.player_speed + 1

                self.players[i]["x"] = self.players[i]["x_f"] - self.players[i]["movement"]

    def remove_player(self):
        """Remove player if it dies.
        It can die if:
        - Falls more than three squares of the map grid
        - Is touched by a saw
        - The player replay the game
        """
        pass
