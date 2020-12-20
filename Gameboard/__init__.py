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
        self.platforms = self.generate_platforms()

        # GATES
        self.entry_gate = self.generate_gate(self.platforms)
        self.exit_gate = self.generate_gate(self.platforms, exit_gate=True)

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
    
    def generate_platforms(self):
        """Create the platforms
        :return list: List with the Platforms
        """
        platforms = []

        row_coordinates = [0]
        # The platform will be on the left or right

        for i in range(self.Constants.platforms_num):
            platforms.append(Platforms())
            platform_row = 0
            
            # platform_row cannot be repeated to avoid overlapping
            while platform_row in row_coordinates:
                # grid_rows - 1 prevents the program from
                # putting a row underneath the platform at the bottom
                platform_row = randint(1, self.Constants.grid_rows - 2)
            
            row_coordinates.append(platform_row)

            platforms[i].width = randint(platforms[i].platform_min_size,
                	                platforms[i].platform_max_size) * self.cell_size
            
            platform_x = ((self.Constants.grid_columns * self.cell_size) -
                          platforms[i].width) / self.cell_size

            platforms[i].x = randint(0, platform_x) * self.cell_size

            platforms[i].y = (platform_row * self.cell_size
                              + self.Constants.scoreboard_height)

        return platforms
    
    def generate_gate(self, platforms, exit_gate=False):
        """Create a gate
            :param platforms (list): List containing self.platforms_num elements
                                    with the following form: [platform_row, platform_size]
            :param exit_gate (bool): True if the gate is the exit_gate
            :return dict: Dict containing the x and y values of the gate
            """
        row_index = randint(0, self.Constants.platforms_num - 1)

        if exit_gate == True:
            # Prevent the two gates from being in the same row
            print(f"entry_gate row index: {int(self.entry_gate.y / self.cell_size)}")
            print(f"exit_gate row index:  {row_index}")
            while row_index == int(self.entry_gate.y / self.cell_size):
                row_index = randint(0, self.Constants.platforms_num - 1)
        

        # We multiply by self.cell_size to get the "coordinates"
        gate_y = platforms[row_index].y

        # Set the x of the gate between the beginning of the platform
        # and the final of it: randint(beginning, final).
        # The 16 allows us to leave a margin between the gate and the end of the platform.
        gate_x = randint((platforms[row_index].x) // self.cell_size + 1,
                         (platforms[row_index].x + platforms[row_index].width)
                         // (self.cell_size - 1))
        gate_x *= self.cell_size

        return Gate(gate_x, gate_y)
