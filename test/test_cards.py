from gaps.cards import Deck, Card, PartialDeck, Suits, Ranks

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
    card1 = Card(Suits.HEARTS, Ranks.THREE)
    card2 = Card(Suits.HEARTS, Ranks.THREE)
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

def test_get_higher_rank():
    assert Ranks.higher_rank(Ranks.ACE) == Ranks.TWO
    assert Ranks.higher_rank(Ranks.TWO) == Ranks.THREE
    assert Ranks.higher_rank(Ranks.THREE) == Ranks.FOUR
    assert Ranks.higher_rank(Ranks.FOUR) == Ranks.FIVE
    assert Ranks.higher_rank(Ranks.FIVE) == Ranks.SIX
    assert Ranks.higher_rank(Ranks.SIX) == Ranks.SEVEN
    assert Ranks.higher_rank(Ranks.SEVEN) == Ranks.EIGHT
    assert Ranks.higher_rank(Ranks.EIGHT) == Ranks.NINE
    assert Ranks.higher_rank(Ranks.NINE) == Ranks.TEN
    assert Ranks.higher_rank(Ranks.TEN) == Ranks.JACK
    assert Ranks.higher_rank(Ranks.JACK) == Ranks.QUEEN
    assert Ranks.higher_rank(Ranks.QUEEN) == Ranks.KING
    assert Ranks.higher_rank(Ranks.KING) == None

def test_get_lower_rank():
    assert Ranks.lower_rank(Ranks.ACE) == None
    assert Ranks.lower_rank(Ranks.TWO) == Ranks.ACE
    assert Ranks.lower_rank(Ranks.THREE) == Ranks.TWO
    assert Ranks.lower_rank(Ranks.FOUR) == Ranks.THREE
    assert Ranks.lower_rank(Ranks.FIVE) == Ranks.FOUR
    assert Ranks.lower_rank(Ranks.SIX) == Ranks.FIVE
    assert Ranks.lower_rank(Ranks.SEVEN) == Ranks.SIX
    assert Ranks.lower_rank(Ranks.EIGHT) == Ranks.SEVEN
    assert Ranks.lower_rank(Ranks.NINE) == Ranks.EIGHT
    assert Ranks.lower_rank(Ranks.TEN) == Ranks.NINE
    assert Ranks.lower_rank(Ranks.JACK) == Ranks.TEN
    assert Ranks.lower_rank(Ranks.QUEEN) == Ranks.JACK
    assert Ranks.lower_rank(Ranks.KING) == Ranks.QUEEN

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
