from tableau import Tableau
import strategies

class Game(object):
    def __init__(self, strategy, visual=False, screen=None):
        S = getattr(strategies, strategy)
        strategy = S()
        self.tableau = Tableau()
        self.redeals = 2
        self.strategy = strategy
        self.visual = visual
        self.screen = screen

    def play(self):
        while True:
            while self.tableau.has_moves():
                if self.visual and self.screen:
                    self.screen.addstr(1,0,self.tableau.dump().encode("utf_8"))
                    self.screen.refresh()
                self.strategy.apply_strategy(self.tableau)
                if self.visual and self.screen:
                    self.screen.getch()
            if not self.tableau.is_complete() and self.redeals > 0:
                self.tableau.redeal()
                self.redeals -= 1
            else:
                break
            
    def in_progress(self):
        return self.tableau.has_moves()

    def game_won(self):
        return self.tableau.is_complete()
