"""
Blocker class.
Allows converting a player into a blocker.
If another player is walking above a platform
and finds a blocker, it changes its direction.
"""
class Blocker:
    def __init__(self, player_x: int, player_y: int):
        self.player_x = player_x
        self.player_y = player_y
        self.img = (0, 0, 16, 16, 16, 0)
    
    # Correct the values with a wrong data type
    # or with a negative value
    @property
    def player_x(self):
        return self.__player_x

    @player_x.setter
    def player_x(self, player_x):
        if player_x < 0 or type(player_x) != int:
            self.__player_x = 0
        else:
            self.__player_x = player_x

    @property
    def player_y(self):
        return self.__player_y

    @player_y.setter
    def player_y(self, player_y):
        if player_y < 0 or type(player_y) != int:
            self.__player_y = 0
        else:
            self.__player_y = player_y
