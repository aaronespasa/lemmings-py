"""
Allow the user to interact with the map
"""
import pyxel
from .Blocker import Blocker
from .Stairs import Stairs
from .Umbrella import Umbrella

class Tools:
    def __init__(self, x: int, y: int, tool: "str"):
        self.x = x
        self.y = y
        self.tool = tool

    @property
    def tool(self):
        return self.__tool
    
    @tool.setter
    def tool(self, tool):
        if tool == "umbrella":
            self.umbrella()
        elif tool == "blocker":
            self.blocker()
        elif tool == "right_stair":
            self.right_stair()
        elif tool == "left_stair":
            self.left_stair()

    def umbrella(self):
        """
        Place an umbrella.
        If the player take it when falling, it won't die.
        """
        umbrella = Umbrella(self.x, self.y)
        return (umbrella.x, umbrella.y, umbrella.img)
    
    def blocker(self):
        """
        Place a blocker.
        If a player reaches a blocker, it'll become a object
        that will change the direction of the lemmings that touch it.
        """
        blocker = Blocker(self.x, self.y)
        return (blocker.x, blocker.y, blocker.img)
    
    def right_stair(self):
        """
        Place a stair with right direction.
        If a player reaches the right stair by the right, it will ascend
        in the right direction.
        If a player reaches the right stair by the left, it will go through it.
        """
        right_s = Stairs(self.x, self.y, "right")
        return (right_s.x, right_s.y, right_s.right, right_s.img)

    def left_stair(self):
        """
        Place a stair with left direction.
        If a player reaches the left stair by the left, it will ascend
        in the left direction.
        If a player reaches the left stair by the right, it will go through it.
        """
        left_s = Stairs(self.x, self.y, "left")
        return (left_s.x, left_s.y, left_s.right, left_s.img)
