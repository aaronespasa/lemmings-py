"""
Constants class.
Contains all the constants for the platforms,
for the grid, for the gate and for the scoreboard
"""

class Constants:
    def __init__(self):
        # GRID:
        self.width = 256
        self.height = 256
        self.grid_rows = 14
        self.grid_columns = 16
        self.cell_size = self.height / self.grid_columns  # 16px

        # SCOREBOARD:
        self.scoreboard_width = self.width
        self.scoreboard_height = self.cell_size * 2

        # PLATFORMS:
        self.platform_min_size = 5
        self.platform_max_size = 10
        self.platforms_num = 7
