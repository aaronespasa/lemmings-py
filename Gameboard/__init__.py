"""
Gameboard class.
"""
from random import randint
from .Platforms import Platforms
from .Gate import Gate
from .Constants import Constants

class Gameboard:
    def __init__(self):
        # CONSTANTS
        self.Constants = Constants()
        self.cell_size = self.Constants.cell_size
        
        # GRID
        self.grid = self.create_grid()
        
        # PLATFORMS
        self.Platform = Platforms()
        self.platforms = self.Platform.generate_platforms()

        # GATES
        # self.entry_gate = self.generate_gate(self.plataforma)
        # self.exit_gate = self.generate_gate(self.plataforma, exit_gate=True)

    def create_grid(self):
        """Create a matrix representing the grid of size grid_rows x grid_columns
        :return list: grid of size rows x columns
        """
        grid = []
        for row in range(self.Constants.grid_rows):
            for column in range(self.Constants.grid_columns):
                # (row + 2) avoid overlapping the grid and the scoreboard
                row_coordinate = self.cell_size * (row + 2)
                column_coordinate = self.cell_size * column

                grid.append([column_coordinate, row_coordinate])
        # print("Matrix of the grid:\n", grid)
        return grid
    
    def generate_gate(self, platforms, entry_gate_index=0, exit_gate=False):
        """Create a gate
            :param platforms (list): List containing self.platforms_num elements
                                    with the following form: [platform_row, platform_size]
            :param exit_gate (bool): True if the gate is the exit_gate
            :return dict: Dict containing the x and y values of the gate
            """
        row_index = randint(0, self.Constants.platforms_num - 1)

        
        if exit_gate == True:
            # Prevent the two gates from being in the same row
            for platform in platforms:                
                while (row_index == entry_gate_index):
                    row_index = randint(0, self.Constants.platforms_num - 1)
                
        else:
            pass
            # while (self.is_inside_platform(platforms[row_index].x, platforms[row_index].y + 16, platforms)):
            #     row_index = randint(0, self.Constants.platforms_num - 1)
            # Avoid creating a gate inside of a platform
            # for platform in platforms:
                # while platform.y == platforms[row_index].y - self.cell_size:
                
        gate_y = platforms[row_index].y

        # Set the x of the gate between the beginning of the platform
        # and the final of it with a margin: randint(beginning + 16, final - 16).
        gate_x = randint((platforms[row_index].x) // self.cell_size + 1,
                         (platforms[row_index].x + platforms[row_index].width)
                         // (self.cell_size) - 1)
        gate_x *= self.cell_size

        return Gate(gate_x, gate_y, row_index)
    
    def is_inside_platform(self, x: int, y: int, platforms: list):
        is_inside = False

        for platform in platforms:
            x_in_platform = x >= platform.x and x <= platform.x + platform.width
            y_in_platform = y == platform.y
            if (x_in_platform and y_in_platform):
                is_inside = True

        return is_inside
    

