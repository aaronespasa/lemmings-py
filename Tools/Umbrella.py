"""
Umbrella class.
If the user is falling and the y of the
player == the y of the umbrella,
the player avoids dying when falling
"""
class Umbrella:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = (0, 16, 0, 16, 16, 0)
    
    # Correct the values with a wrong data type
    # or with a negative value
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        else:
            self.__x = x

#    # @property
    # def y(self):
    #     return self.__y

    # @x.setter
    # def y(self, y):
    #     if y < 0:
    #         self.__y = 0
    #     else:
    #         self.__y = y
