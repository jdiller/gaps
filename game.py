from tableau import Tableau
from strategies import MoveLeftMostMoveable

class Game(object):
    def __init__(self):
        self.tableau = Tableau()
        self.redeals = 2
        self.strategy = MoveLeftMostMoveable()

    def play(self):
        while True:
            while self.tableau.has_moves():
                self.strategy.apply_strategy(self.tableau)
            if not self.tableau.is_complete() and self.redeals > 0:
                self.tableau.redeal()
                self.redeals -= 1
            else:
                break


    def in_progress(self):
        return self.tableau.has_moves()

    def game_won(self):
        return self.tableau.is_complete()
