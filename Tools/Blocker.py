"""
Blocker class.
Allows converting a player into a blocker.
If another player is walking above a platform
and finds a blocker, it changes its direction.
"""
class Blocker:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.img = (0, 0, 16, 16, 16, 0)
    
    # Correct the values with a wrong data type
    # or with a negative value
    # @property
    # def x(self):
    #     return self.__x

    # @x.setter
    # def x(self, x):
    #     if x < 0 or type(x) != int:
    #         self.__x = 0
    #     else:
    #         self.__x = x

    # @property
    # def y(self):
    #     return self.__y

    # @y.setter
    # def y(self, y):
    #     if y < 0 or type(y) != int:
    #         self.__y = 0
    #     else:
    #         self.__y = y
