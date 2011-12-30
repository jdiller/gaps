from cards import Ranks

class MoveLeftMostMoveable(object):
    #always finds and moves left-most card that can be moved
    def apply_strategy(self, tableau):
        moveables = tableau.find_moveable()
        left_most = None
        for m in moveables:
            if left_most is None or left_most[1] > m[1]:
                left_most = m
        gap = tableau.find_gap_for_moveable(left_most)
        tableau.swap(left_most, gap)

class MoveRightMostMoveable(object):
     #always finds and moves right-most card that can be moved
    def apply_strategy(self, tableau):
        moveables = tableau.find_moveable()
        right_most = None
        for m in moveables:
            if right_most is None or right_most[1] < m[1]:
                right_most = m
        gap = tableau.find_gap_for_moveable(right_most)
        tableau.swap(right_most, gap)

class FillRightMostGap(object):
    #always tries to fill the right-most gap
    def apply_strategy(self, tableau):
        gaps = tableau.find_gaps()
        right_most = None
        for g in gaps:
            if right_most is None or right_most[1] < g[1]:
                if tableau.find_moveable_for_gap(g) is not None:
                    right_most = g

        moveable = tableau.find_moveable_for_gap(right_most)
        tableau.swap(right_most, moveable)

class MoveHighestRankFirst(object):
    def apply_strategy(self, tableau):
        moveables = tableau.find_moveable()
        highest = None
        for m in moveables:
            if highest is None or \
                tableau.card_at(highest).rank[1] < tableau.card_at(m).rank[1]:
                    highest = m

        gap = tableau.find_gap_for_moveable(highest)
        tableau.swap(highest, gap)

class MoveLowestRankFirst(object):
    def apply_strategy(self, tableau):
        moveables = tableau.find_moveable()
        lowest = None
        for m in moveables:
            if lowest is None or \
                tableau.card_at(lowest).rank[1] > tableau.card_at(m).rank[1]:
                    lowest = m

        gap = tableau.find_gap_for_moveable(lowest)
        tableau.swap(lowest, gap)

class AvoidMakingBlockingGaps(object):
    def apply_strategy(self, tableau):
        moveables = tableau.find_moveable()
        candidates = []
        for m in moveables:
            if m[1] == 0 or \
                    tableau.card_at((m[0],m[1]-1)) is None or \
                    tableau.card_at((m[0],m[1]-1)).rank != Ranks.KING:
                candidates.append(m)
        if len(candidates) > 0:
            gap = tableau.find_gap_for_moveable(candidates[0])
            tableau.swap(gap, candidates[0])
        else:
            backup_strategy = FillRightMostGap()
            backup_strategy.apply_strategy(tableau)

