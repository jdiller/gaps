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
        ret = ""
        for i in range(0,4):
            row = ""
            for j in range(0,13):
                if self.card_at((i,j)) is None:
                    row += "[     ] "
                else:
                    row += self.card_at((i,j)).short() + " "
            ret += row + "\n"
        return ret

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

    def redeal(self):
        cards_to_redeal = []
        i = 0
        for row in self.grid:
            rank = 1
            j = 0
            remove_rest = False
            for card in row:
                if card is None:
                    remove_rest = True
                elif remove_rest or card.rank != Ranks.all_ranks[rank]:
                    cards_to_redeal.append(card)
                    self.grid[i][j] = None
                    remove_rest = True
                else:
                    rank = rank + 1
                    if rank >= len(Ranks.all_ranks):
                        remove_rest = True
                j = j + 1
            i = i + 1
        cards_to_redeal.reverse()
        for i in range(len(self.grid)):
            gap_in_row = False
            for j in range(len(self.grid[i])):
                if self.grid[i][j] is None:
                    if gap_in_row:
                        self.grid[i][j] = cards_to_redeal.pop()
                    else:
                        gap_in_row = True


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

    def find_gap_for_moveable(self, moveable):
        moveable_card = self.card_at(moveable)
        if moveable_card.rank == Ranks.TWO:
            gaps = [g for g in self.find_gaps() if g[1] == 0]
            return gaps[0]
        else:
            target_loc = self.find_card(Card(moveable_card.suit,
                    Ranks.lower_rank(moveable_card.rank)))

            target_loc = (target_loc[0], target_loc[1]+1)
            return target_loc

    def find_moveable_for_gap(self, gap):
        if gap[1] == 0:
            twos = [pos for pos in self.find_by_rank(Ranks.TWO) if pos[1] > 0]
            return twos[0]

        neighbour = self.card_at((gap[0], gap[1]-1))
        loc = None
        if neighbour != None and neighbour.rank != Ranks.KING:
            loc = self.find_card(Card(neighbour.suit,
                Ranks.higher_rank(neighbour.rank)))
        return loc

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

