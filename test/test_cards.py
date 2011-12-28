from gaps.cards import Deck, Card

def test_deck_has_52_cards():
    d = Deck()
    assert len(d.cards) == 52

def test_shuffled_deck_has_52_cards():
    d = Deck()
    d.shuffle()
    assert len(d.cards) == 52

def test_shuffled_deck_has_no_duplicates():
    d = Deck()
    d.shuffle()
    #unshuffle
    cards = sorted(d.cards, key = lambda card: card.suit[1] * 100 +
            card.rank[1])

    #should look like a new deck
    new_deck = Deck()
    for i in range(len(cards)):
        assert cards[i].rank == new_deck.cards[i].rank and \
                cards[i].suit == new_deck.cards[i].suit

def test_card_equality():
    card1 = Card(Card.suits[2], Card.ranks[3])
    card2 = Card(Card.suits[2], Card.ranks[3])
    assert card1 == card2
