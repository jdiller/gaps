import cards

class Tableau(object):
    def __init__(self):
        self.grid = []
        deck = cards.Deck()
        deck.shuffle()

        for i in range(1,5):
            self.grid.append([])
            for j in range(1, 14):
                card = deck.cards[(i*j) - 1]
                if card.rank[0] == "A":
                    card = None
                self.grid[i-1].append(card)

    def dump(self):
        for i in range(0,4):
            row = ""
            for j in range(0,13):
                if self.grid[i][j] is None:
                    row += "[     ] "
                else:
                    row += self.grid[i][j].short() + " "
            print row

