from random import randint

class Player:
    def __init__(self, entry_gate, exit_gate):
        self.entry_gate = entry_gate
        self.exit_gate = exit_gate
        self.players = []
        self.player_stats = {
            "x": self.entry_gate["x"],
            "y": self.entry_gate["y"],
            "alive": True
        }
        self.players_num = randint(10, 20)
        for _ in range(self.players_num):
            self.players.append(self.player_stats)
        

    def create_player(self):
        """Assign it a position"""
        pass

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
