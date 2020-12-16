"""
Create a matrix representation of the grid.
This grid will be useful to the user to
interact with the game.
"""
class Gameboard:
    def __init__(self):
        # DIMENSIONS:
        self.width = 256
        self.height = 256
        self.grid_rows = 14
        self.grid_columns = 16
        self.cell_size = self.height / self.grid_columns  # 16px

        # COLORS
        self.WHITE = 7
        self.DARK_BLUE = 1

        # REPRESENTATION OF THE SCOREBOARD AND THE GRID
        self.scoreboard = {
            "x": 0,
            "y": 0,
            "width": self.width,
            "height": self.cell_size * 2,
            "bgcolor": self.DARK_BLUE,
            "textcolor": self.WHITE,
            "level": "",
            "alive": "",
            "saved": "",
            "died": "",
            "ladders": "",
            "umbrellas": "",
            "blockers": ""
        }
        # The grid does not include the scoreboard
        self.grid = self.create_grid(
            self.grid_rows, self.grid_columns, self.cell_size)

        # pyxel.init(self.width, self.height, caption=self.pyxel_window_title)
        # pyxel.run(self.exit_option, self.draw_gameboard)

    def create_grid(self, grid_rows, grid_columns, cell_size):
        """Create a matrix representing the grid of size grid_rows x grid_columns
        :param grid_rows (int): Total number of rows
        :param grid_columns (int): Total number of columns
        :para cell_size(int): Size of the cell
        :return list: grid of size grid_rows x grid_columns
        """
        grid = []
        for row in range(grid_rows):
            for column in range(grid_columns):
                # (row + 2) avoid overlapping the grid and the scoreboard
                row_coordinate = self.cell_size * (row + 2)
                column_coordinate = self.cell_size * column

                grid.append([column_coordinate, row_coordinate])

        # print("Matrix of the grid:\n", grid)
        return grid

Gameboard()
