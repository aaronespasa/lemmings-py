"""
Stairs class.
This class includes both the right and the left stairs.
The direction of them is determined by the variable direction.
"""
class Stairs:
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.cell_size = 16
        
        # self.left and self.right are the coordinates
        # of the two types of stairs (determined by the var direction)
        self.left = {
            "bottom_right": [x, y],
            "top_left": [x, y],
        }
        self.right = {
            "bottom_left": [x, y],
            "top_right": [x, y],
        }

        self.direction = direction
        self.img = (0, 0, 0, 16, 16, 0)

    # Correct the values with a wrong data type
    # or with a negative value
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0 or type(x) != int:
            self.__x = 0
        else:
            self.__x = x
    
    @property
    def y(self):
        return self.__y

    @x.setter
    def y(self, y):
        if y < 0 or type(y) != int:
            self.__y = 0
        else:
            self.__y = y
    
    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, left: list):
        if self.direction == "left":
            left["bottom_right"] = [self.__x + self.cell_size, self.__y + self.cell_size]
            left["top_left"] = [self.__x, self.__y]
    
    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right: list):
        if self.direction == "right":
            right["bottom_left"] = [self.__x, self.__y + self.cell_size]
            right["top_right"] = [self.__x + self.cell_size, self.__y]
    
