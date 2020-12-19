"""
Allow the user to interact with the map
"""
import pyxel
from .Blocker import Blocker
from .Stairs import Stairs
from .Umbrella import Umbrella

class Tools:
    def __init__(self, grid, cell_size):
        self.tools = {
            "upper_stairs": None,
            "down_stairs": None,
            "umbrella": None,
            "blocker": None
        }
        self.grid = grid
        self.cell_size = cell_size
    
    def tool(self, x, y):        
        square = self.detect_cell(x, y)
        selected_tool = None
        return (square, selected_tool)

    def detect_cell(self, x, y):
        if x >= 240 and y >= 240:
            return [240, 240]

        if x >= 240:
            x_sq = 240
            for i in range(len(self.grid)):
                if self.grid[i][1] <= y and self.grid[i + 1][1] > y:
                    y_sq = self.grid[i][1]
                    return [x_sq, y_sq]
        if y >= 240:
            y_sq = 240
            for i in range(len(self.grid)):
                if self.grid[i][0] <= x and self.grid[i + 1][0] > x:
                    x_sq = self.grid[i][0]
                    return [x_sq, y_sq]


        for i in range(len(self.grid)):
            if self.grid[i][0] <= x and self.grid[i + 1][0] > x:
                x_sq = self.grid[i][0]

            if self.grid[i][1] <= y and self.grid[i + 1][1] > y:
                y_sq = self.grid[i][1]

        return [x_sq, y_sq]