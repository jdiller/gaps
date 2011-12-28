import cards

class Tableau(object):
    def __init__(self):
        self.grid = []
        deck = cards.Deck()
        deck.shuffle()
        n = 0
        for i in range(1,5):
            self.grid.append([])
            for j in range(1, 14):
                card = deck.cards[n]
                if card.rank[0] == "A":
                    card = None
                self.grid[i-1].append(card)
                n += 1

    def dump(self):
        for i in range(0,4):
            row = ""
            for j in range(0,13):
                if self.grid[i][j] is None:
                    row += "[     ] "
                else:
                    row += self.grid[i][j].short() + " "
            print row

    def has_moves(self):
        for i in range(0,4):
            for j in range(0, len(self.grid[i])):
                    if self.grid[i][j] is None:
                        if j == 0 or self.grid[i][j-1].rank[0] != "K":
                            return True
        return False

    def is_complete(self):
        for i in range(0,4):
            if self.grid[i][0] is None or self.grid[i][0].rank[0] != "2":
                return False
            for j in range(1, len(self.grid[i])-1):
                if self.grid[i][j] is None:
                    return False
                if self.grid[i][j].suit != self.grid[i][j-1].suit and \
                        self.grid[i][j].rank[1] != self.grid[i][j-1].rank[1] - 1:
                    return False
        return True

    def find_gaps(self):
        gaps = []
        for i in range(4):
            for j in range(13):
                if self.grid[i][j] is None:
                    gaps.append((i,j))
        return gaps

    def find_kings(self):
        king = ("K", 13)
        return self.find_by_rank(king)

    def find_by_rank(self, rank):
        found = []
        for i in range(4):
            for j in range(13):
                if self.grid[i][j] is not None and self.grid[i][j].rank == rank:
                    found.append((i,j))
        return found

    def flatten(self):
        ret = []
        for i in range(4):
            for j in range(13):
                if not self.grid[i][j] is None:
                    ret.append(self.grid[i][j])
        return ret

