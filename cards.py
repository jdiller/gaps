# -*- coding: utf-8 -*-
from random import randrange

def __init__():
    pass

class Suits(object):
    HEARTS = ("Hearts", 0)
    CLUBS = ("Clubs", 1)
    DIAMONDS = ("Diamonds", 2)
    SPADES = ("Spaces", 3)

    all_suits  = [HEARTS, CLUBS, DIAMONDS, SPADES]

class Ranks(object):
    ACE = ("A", 1)
    TWO = ("2", 2)
    THREE = ("3", 3)
    FOUR = ("4", 4)
    FIVE = ("5", 5)
    SIX = ("6", 6)
    SEVEN = ("7", 7)
    EIGHT = ("8", 8)
    NINE = ("9", 9)
    TEN = ("10",10)
    JACK = ("J", 11)
    QUEEN = ("Q", 12)
    KING = ("K", 13)

    all_ranks =[ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, \
            JACK, QUEEN, KING]

    @classmethod
    def lower_rank(cls, rank):
        if rank == cls.ACE:
            return None
        return cls.all_ranks[cls.all_ranks.index(rank) - 1]

    @classmethod
    def higher_rank(cls, rank):
        if rank == cls.KING:
            return None
        return cls.all_ranks[cls.all_ranks.index(rank) + 1]

class Card(object):

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
        for suit in Suits.all_suits:
            for rank in Ranks.all_ranks:
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
