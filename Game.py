from Player import Player
from GameGrid import GameGrid

# I would have a large class like this to contain everything and run the game updates. Again this could be a kivy class
class Game:
    def __init__(self, game_grid: GameGrid, player: Player):
        self.game_grid = game_grid
        self.player = player
