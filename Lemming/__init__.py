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

        # players_num = randint(10, 20)
        
        players_num = 1

        for i in range(players_num):
            players.append(Player(self.x, self.y))
            players[i].x_i = self.x

        return players

    def update_player(self):
        """Move autonomously"""
        for i in range(len(self.players)):
            # MAIN PLAYER PROPERTIES
            is_falling = self.is_falling(self.players[i])
            
            # DIRECTION
            # The 12 is the width of the player without any space
            if self.players[i].x > self.width - 12:
                # Player at the right of the window
                self.players[i].direction = "left"
            elif self.players[i].x < -4:
                # Player at the left of the window
                self.players[i].direction = "right"

            # X MOVEMENT
            if is_falling == False:
                if self.players[i].direction == "left":
                    self.players[i].x -= self.players[i].speed
                elif self.players[i].direction == "right":
                    self.players[i].x += self.players[i].speed
            
            # Y MOVEMENT
            if is_falling:
                # Add umbrella here
                self.players[i].y += self.players[i].speed

            # self.players[i].falling = self.is_falling(self.players[i])

            # if self.players[i].falling == False:
            #     # IS NOT FALLING
            #     # The player is not falling by default, so this conditional
            #     # will be initially satisfied and the variables player_time_y
            #     # and self.players[i].y_before_falling will be assigned
            #     for platform in self.platforms:
            #         if self.players[i].y == platform.y:
            #             self.players[i].y_before_falling = platform.y
                
            #     self.x_move(self.players[i])
            #     self.player_time_y = time()
            #     self.players[i].time_x_bef_falling = time()
            # else:
            #     # IS FALLING
            #     self.players[i].movement = ((time() - self.players[i].player_time_y)
            #                                 * (self.players[i].speed / 2))

            #     self.players[i].y = self.players[i].y_before_falling - 26 + self.players[i].movement

            #     self.players[i].time_x_falling = time() - self.players[i].time_x_bef_falling
        
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


    def x_move(self, player):
        """Movement on the x axis"""
        pass
        # The 10 is the width of the player without any space
        # if player.x > self.width - 10:
        #     # Player at the right of the window
        #     player.direction = "left"
        #     player.start = False
        #     player.player_time_x = time()

        # elif player.x < 0:
        #     # Player at the left of the window
        #     player.direction = "right"
        #     player.player_time_x = time()
        
        # # If the player finds a platform, it changes
        # # its direction
        # for platform in self.platforms:
        #     if (int(player.x) == platform.x and
        #         int(player.y) == platform.y):
        #         if player.direction == "right":
        #             player.direction == "left"
        #         elif player.direction == "left":
        #             player.direction == "right"
        
        # # Increase the movement in the correct direction
        # if player.direction == "right":
            
        #     player.movement = ((
        #         time() - (player.player_time_x + player.time_x_falling))
        #         * player.speed)

        #     if player.start == True:        
        #         player.x = player.x_i + player.movement
        #     else:
        #         player.x = player.movement
        
                            
        #     # Get the final x of the player before changing its direction 
        #     player.x_f = player.x
            
        # elif player.direction == "left":
        #     # The + 1 allows us to avoid enter on a loop
        #     # because of the player["x"] < 0 condition
        #     player.movement = (
        #         time() - player.player_time_x) * player.speed + 1

        #     player.x = player.x_f - player.movement

    def remove_player(self):
        """Remove player if it dies.
        It can die if:
        - Falls more than one square (16px) without an umbrella
        """
        pass
