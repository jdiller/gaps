from cards import Card, Deck, Ranks, Suits

class Tableau(object):
    def __init__(self):
        self.grid = []
        deck = Deck()
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
                if self.card_at((i,j)) is None:
                    row += "[     ] "
                else:
                    row += self.card_at((i,j)).short() + " "
            print row

    def has_moves(self):
        for i in range(0,4):
            for j in range(0, len(self.grid[i])):
                    if self.card_at((i,j)) is None \
                            and self.card_at((i,j-1)) is not None: 
                        if j == 0 or self.card_at((i, j-1)).rank != Ranks.KING:
                            return True
        return False

    def is_complete(self):
        for i in range(0,4):
            if self.grid[i][0] is None or self.grid[i][0].rank != Ranks.TWO:
                return False
            for j in range(1, len(self.grid[i])-1):
                if self.card_at((i,j)) is None:
                    return False
                if self.card_at((i,j)).suit != self.card_at((i,j-1)).suit and \
                        self.card_at((i,j)).rank[1] != self.card_at((i,j-1)).rank[1] - 1:
                    return False
        return True

    def swap(self, location1, location2):
        row1 = location1[0]
        col1 = location1[1]
        row2 = location2[0]
        col2 = location2[1]

        self.grid[row1][col1], self.grid[row2][col2] = \
            self.grid[row2][col2], self.grid[row1][col1]
    def find_gaps(self):
        gaps = []
        for i in range(4):
            for j in range(13):
                if self.card_at((i,j)) is None:
                    gaps.append((i,j))
        return gaps

    def find_kings(self):
        king = ("K", 13)
        return self.find_by_rank(king)

    def find_moveable(self):
        gaps = self.find_gaps()
        moveable = []
        for g in gaps:
            if g[1] == 0:
                twos = self.find_by_rank(Ranks.TWO)
                for two in twos:
                    if not two[1] == 0:
                        moveable.append(two)
            else:
                neighbour = self.card_at((g[0], g[1]-1))
                if neighbour != None and neighbour.rank != Ranks.KING:
                    next_rank = Ranks.higher_rank(neighbour.rank)
                    moveable_card = Card(neighbour.suit, next_rank)
                    moveable_loc = self.find_card(moveable_card)
                    moveable.append(moveable_loc)
        return moveable

    def find_card(self, card):
        found = self.find_by_rank(card.rank)
        for f in found:
            foundcard = self.card_at(f)
            if foundcard.suit == card.suit:
                return f
        return None


    def find_by_rank(self, rank):
        found = []
        for i in range(4):
            for j in range(13):
                if self.card_at((i,j)) is not None and self.card_at((i,j)).rank == rank:
                    found.append((i,j))
        return found

    def card_at(self, coords):
        return self.grid[coords[0]][coords[1]]

    def flatten(self):
        ret = []
        for i in range(4):
            for j in range(13):
                if not self.card_at((i,j)) is None:
                    ret.append(self.card_at((i,j)))
        return ret

