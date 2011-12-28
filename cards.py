# -*- coding: utf-8 -*-
from random import randrange

def __init__():
    pass

class Card(object):
    ranks = [("A", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6),
            ("7", 7), ("8", 8), ("9", 9), ("10",10),  ("J", 11), 
            ("Q", 12), ("K", 13)]

    suits  = [("Hearts", 0), ("Clubs", 1), ("Diamonds", 2), ("Spades", 3)]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def short(self):
        return "[%s %s ]" % (self.rank[0].ljust(2), self.short_suit())

    def short_suit(self):
        shorts = ["♥","♣", "♦", "♠"]
        return shorts[self.suit[1]]

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        i = len(self.cards)
        while i > 1:
            i -= 1
            j = randrange(i)
            self.cards[j], self.cards[i] = self.cards[i], self.cards[j]

    def dump(self):
        for c in self.cards:
            print c.short()

class PartialDeck(Deck):
    def __init__(self, cards):
        self.cards = cards
