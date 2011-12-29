from gaps.cards import Deck, Card, PartialDeck

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
    cards = unshuffle(d.cards) 

    #should look like a new deck
    new_deck = Deck()
    assert compare_cards(cards, new_deck.cards)

def test_card_equality():
    card1 = Card(Card.suits[2], Card.ranks[3])
    card2 = Card(Card.suits[2], Card.ranks[3])
    assert card1 == card2

def test_can_make_partial_deck():
    d = Deck()
    i = 0
    stack = []
    while i < len(d.cards):
        stack.append(d.cards[i])
        i += 2
    assert len(stack) == 26
    control_deck = list(stack)

    partial = PartialDeck(stack)
    partial.shuffle()
    assert compare_cards(unshuffle(partial.cards), control_deck)

def unshuffle(cards):
    return  sorted(cards, key = lambda card: card.suit[1] * 100 + card.rank[1])

def compare_cards(deck1, deck2):
    if len(deck1) != len(deck2):
        return False

    result = True
    for i in range(len(deck1)):
        result = result and  deck1[i].rank == deck2[i].rank and \
                deck1[i].suit == deck2[i].suit

    return result
