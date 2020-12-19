"""
Lemming class.
Creation of the Lemming and adding physics to it.
We used the library time instead of pyxel.frame_count
because it gave us more flexibility to change the speed.
"""
from time import time
from random import randint
from .Player import Player

class Lemming:
    def __init__(self, x: int, y: int, platforms: list):
        self.x = x
        self.y = y
        self.width = 256
        self.players = self.create_players()
        self.platforms = platforms
        

    def create_players(self):
        """Create a number of players between 10 and 20
        and assign to each one of them the coordinates x and y
        and also if the player is alive."""
        players = []

        players_num = randint(10, 20)
        
        for i in range(players_num):
            players.append(Player(self.x, self.y))
            players[i].x_i = self.x

        return players

    def update_player(self):
        """Move autonomously"""
        for i in range(len(self.players)):
            # self.x_move()
            self.players[i].falling = self.is_falling(self.players[i])

            if self.players[i].falling == False:
                # IS NOT FALLING
                # The player is not falling by default, so this conditional
                # will be initially satisfied and the variables player_time_y
                # and self.players[i].y_before_falling will be assigned
                for platform in self.platforms:
                    if self.players[i].y == platform.y:
                        self.players[i].y_before_falling = platform.y
                
                self.x_move()
                self.player_time_y = time()
            else:
                # IS FALLING
                self.players[i].movement = int((time() - self.players[i].player_time_y)
                                            * (self.players[i].speed / 2))

                self.players[i].y = self.players[i].y_before_falling - 26 + self.players[i].movement
                # print(self.players[i].y)
        
        return self.players

    def is_falling(self, player):
        """Check if the user is falling"""
        # Fall if there's not a platform underneath the player
        for platform in self.platforms:
            
            if player.y == platform.y:
                # Set the final x of the platform
                platform_x_f = platform.x + platform.width

                player_in_platform = player.x >= platform.x and (
                                     player.x <= platform_x_f)

                if player_in_platform:
                    return False
        
        # Check also is the user is above a stair
        
        return True


    def x_move(self):
        """Movement on the x axis"""
        for i in range(len(self.players)):
            # The 10 is the width of the player without any space
            if self.players[i].x > self.width - 10:
                # Player at the right of the window
                self.players[i].direction = "left"
                self.players[i].start = False
                self.players[i].player_time_x = time()

            elif self.players[i].x < 0:
                # Player at the left of the window
                self.players[i].direction = "right"
                self.players[i].player_time_x = time()
            
            # Increase the movement in the correct direction
            if self.players[i].direction == "right":
                
                self.players[i].movement = (
                    time() - self.players[i].player_time_x) * self.players[i].speed

                if self.players[i].start == True:        
                    self.players[i].x = self.players[i].x_i + self.players[i].movement
                else:
                    self.players[i].x = self.players[i].movement
                                
                # Get the final x of the player before changing its direction 
                self.players[i].x_f = self.players[i].x
                
            elif self.players[i].direction == "left":
                # The + 1 allows us to avoid enter on a loop
                # because of the self.players[i]["x"] < 0 condition
                self.players[i].movement = (
                    time() - self.players[i].player_time_x) * self.players[i].speed + 1

                self.players[i].x = self.players[i].x_f - self.players[i].movement

    def remove_player(self):
        """Remove player if it dies.
        It can die if:
        - Falls more than one square (16px) without an umbrella
        """
        pass
