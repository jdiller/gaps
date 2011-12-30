# -*- coding: utf-8 -*-
from gaps.tableau import Tableau
from gaps.cards import Card, Suits, Ranks

def test_tableau_has_four_rows():
    t = Tableau()
    assert len(t.grid) == 4

def test_tableau_has_thirteen_columns():
    t = Tableau()
    for i in range(0,4):
        assert len(t.grid[i]) == 13

def test_has_moves_returns_true_for_new_tableau():
    t = Tableau()
    assert t.has_moves()

def test_complete_returns_false_for_new_tableau():
    t = Tableau()
    assert not t.is_complete()

def test_has_moves_returns_false_for_winning_tableau():
    t = winning_tableau()
    assert not t.has_moves()

def test_can_detect_winning_tableau():
    tab = winning_tableau()
    assert tab.is_complete()

def test_can_detect_busted_tableau():
    for i in range(1000):
        tab = busted_tableau()
        assert not tab.has_moves()
        assert not tab.is_complete()

def test_no_moveables_in_busted_tableau():
    tab = busted_tableau()
    moveables = tab.find_moveable()
    assert len(moveables) == 0

def test_no_moveables_in_winning_tableau():
    tab = winning_tableau()
    moveables = tab.find_moveable()
    assert len(moveables) == 0

def test_new_tableau_has_moveables():
    for i in range(1000):
        tab = Tableau()
        while not tab.has_moves():
            tab = Tableau()
        moveables = tab.find_moveable()
        assert len(moveables) > 0

def test_moveables_are_moveable():
    for i in range(1000):
        tab = Tableau()
        while not tab.has_moves():
            tab = Tableau()
        moveables = tab.find_moveable()
        for m in moveables:
            card = tab.card_at(m)
            if card.rank == Ranks.TWO:
                left_gaps = [gap for gap in tab.find_gaps() if gap[1] == 0]
                assert len(left_gaps) > 0
            else:
                target_card = Card(card.suit, Ranks.lower_rank(card.rank))
                assert target_card is not None
                target_loc = tab.find_card(target_card)
                assert tab.card_at((target_loc[0], target_loc[1]+1)) is None 

def test_can_find_every_card():
    tab = Tableau()
    for row in range(len(tab.grid)):
        for col in range(len(tab.grid[row])):
            card = tab.card_at((row,col))
            if card is not None:
                loc = tab.find_card(card)
                assert loc[0] == row and loc[1] == col

def test_can_find_gaps():
    #because tabs start random, repeat a bunch of times to compensate
    for i in range(1000):
        tab = Tableau()
        gaps = tab.find_gaps()
        assert len(gaps) == 4
        for g in gaps:
            assert tab.grid[g[0]][g[1]] is None

def test_can_find_kings():
    #because tabs start random, repeat a bunch of times to compensate
    king = Ranks.KING
    for i in range(1000):
        tab = Tableau()
        kings = tab.find_kings()
        assert len(kings) == 4
        for k in kings:
            assert tab.grid[k[0]][k[1]].rank == king

def test_can_swap_cards():
    tab = Tableau()
    pos1 = (1,1)
    pos2 = (1,12)
    card1_before = tab.card_at(pos1)
    card2_before = tab.card_at(pos2)
    tab.swap(pos1, pos2)
    card1_after = tab.card_at(pos1)
    card2_after = tab.card_at(pos2)
    assert card1_after == card2_before
    assert card2_after == card1_before

def winning_tableau():
    tab = Tableau()
    for i in range(4):
        for j in range(1,13):
            card = Card(Suits.all_suits[i],Ranks.all_ranks[j])
            tab.grid[i][j-1] = card
        tab.grid[i][12] = None
    tab.dump()
    return tab

def busted_tableau():
    tab = Tableau()
    kings = tab.find_kings()
    continue_loop = True
    loop_counter = 0
    while continue_loop:
        if loop_counter > 100:
            tab = Tableau()
        gaps = tab.find_gaps()
        kings = tab.find_kings()
        i = 0
        for g in gaps:
            gap_row = g[0]
            gap_col = g[1]
            king_row = kings[i][0]
            king_col = kings[i][1]
            if gap_col == 0:
                tab.grid[gap_row][0],tab.grid[king_row][king_col] = \
                    tab.grid[king_row][king_col], None
            else:
                tab.grid[gap_row][gap_col-1], tab.grid[king_row][king_col] = \
                tab.grid[king_row][king_col], tab.grid[gap_row][gap_col-1]
            i += 1
        kings = tab.find_kings()
        continue_loop = False
        for king in kings:
            try:
                if king[1] == 12 or tab.grid[king[0]][king[1]+1] is not None:
                    continue_loop = True
                    loop_counter += 1
                    break
            except IndexError as ex:
                print king
                raise ex

    assert len(tab.find_gaps()) == 4
    assert len(tab.find_kings()) == 4
    return tab
