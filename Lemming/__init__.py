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
        self.lemmings_num = 5
        # randint(10, 20)
        self.players = self.create_players()
        self.platforms = platforms
        
    def create_players(self):
        """Create a number of players between 10 and 20
        and assign to each one of them the coordinates x and y
        and also if the player is alive."""
        players = []

        for i in range(self.lemmings_num):
            players.append(Player(self.x, self.y))
            players[i].x_i = self.x

        return players
    
    def before_start(self):
        return self.players

    def update_player(self, tools):
        """Move autonomously"""
        # TOOLS
        umbrellas = tools["umbrella"]  # [umbrella_x, umbrella_y, umbrella_img]
        blockers = tools["blocker"]
        right_stairs = tools["right_s"]
        left_stairs = tools["left_s"]

        players_to_remove = []

        for i in range(len(self.players[:])):
            if self.players[i].alive:
                # MAIN PLAYER PROPERTIES
                is_falling = self.is_falling(self.players[i])
                hit_platform_by_side = self.hit_platform_by_side(self.players[i])

                is_touching_umbrella, umbrella_idx = self.is_touching_tool(self.players[i], umbrellas)
                is_touching_blocker, blocker_idx = self.is_touching_tool(self.players[i], blockers)
                is_touching_right_stair, right_stair_idx = self.is_touching_tool(self.players[i], right_stairs)
                is_touching_left_stair, left_stair_idx = self.is_touching_tool(self.players[i], left_stairs)

                # DIRECTION
                # The 12 is the width of the player without any space
                if self.players[i].x > self.width - 12:
                    # Player at the right of the window
                    self.players[i].direction = "left"
                elif self.players[i].x < -4:
                    # Player at the left of the window
                    self.players[i].direction = "right"
                elif hit_platform_by_side and is_falling == False:
                    # Player has collided with a platform
                    self.change_direction(self.players[i])
                elif is_touching_blocker and is_falling == False:
                    # Player has collided with a blocker
                    self.change_direction(self.players[i])

                # X MOVEMENT
                if is_falling == False:
                    if self.players[i].direction == "left":
                        self.players[i].x -= self.players[i].speed
                    elif self.players[i].direction == "right":
                        self.players[i].x += self.players[i].speed

                # Y MOVEMENT
                if is_falling:
                    self.players[i].y += self.players[i].speed * 2
                    
                    if is_touching_umbrella:
                        self.players[i].umbrella = True
                
                if is_touching_right_stair:
                    print("Right stair")
                
                if is_touching_left_stair:
                    print("Left stair")
                
                # Check if the player has died falling
                for platform in self.platforms:
                    if self.players[i].y == platform.y:
                        # Set the final x of the platform
                        platform_x_f = platform.x + platform.width

                        player_in_platform = self.players[i].x >= platform.x and (
                                             self.players[i].x <= platform_x_f)
                        
                        if is_falling and player_in_platform and self.players[i].umbrella == False:
                            players_to_remove.append(i)


                # Check if the player has dead going underneath the window
                if self.players[i].y > 255:
                    players_to_remove.append(i)
        
        if len(players_to_remove) >= 1:
            self.remove_player(players_to_remove)
                
        return self.players

    def is_falling(self, player):
        """Check if the user is falling"""
        # Fall if there's not a platform underneath the player
        for platform in self.platforms:
            
            # If self.players[i].speed is a flot, change player.y
            # by int(player.y)
            if player.y == platform.y:
                # Set the final x of the platform
                platform_x_f = platform.x + platform.width

                player_in_platform = player.x >= platform.x and (
                                     player.x <= platform_x_f)

                if player_in_platform:
                    return False
        
        # Check also is the user is above a stair
        
        return True

    def hit_platform_by_side(self, player):
        """Check if the player is hitting a platform by its side"""
        is_hitting_platform = False

        for platform in self.platforms:
            x_equal = player.x == platform.x or \
                      player.x == platform.x + platform.width
            y_equal = player.y - 16 == platform.y

            if (x_equal and y_equal):
                is_hitting_platform = True
        
        return is_hitting_platform
    
    def is_touching_tool(self, player, tool):
        """Check if the player is in contact with a tool
        :return: (bool, tool_index)
        """
        is_touching = False
        tool_index = 0

        for i in range(len(tool)):
            x_near_tool = player.x > tool[i][0] - 2 and player.x < tool[i][0] + 2
            if x_near_tool and player.y - 16 == tool[i][1]:
                is_touching = True
                tool_index = i
        
        return (is_touching, tool_index)
    
    def change_direction(self, player):
        """Change the direction of the player"""
        if player.direction == "right":
            player.direction = "left"
        elif player.direction == "left":
            player.direction = "right"

    def convert_in_blocker(self, player):
        """Convert the player into a blocker"""
        pass

    def remove_player(self, players: list):
        """Remove player if it dies.
        It can die if:
        - Falls more than one square (16px) without an umbrella
        """
        for i in players:
            self.players[i].alive = False
            self.players[i].img = (0, 32, 40, 16, 12, 0) # dead img
            
