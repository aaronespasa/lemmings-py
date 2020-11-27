class Player():
    total_lemmings: int

    def create_player(self):
        """Assign it a position"""
        x: int
        y: int 

    def update_player(self, x, y):
        """Move autonomously"""
        pass

    def remove_player(self):
        """Remove player if it dies.
        It can die if:
        - Falls more than three squares of the map grid
        - Is touched by a saw
        - The player replay the game
        """
        pass