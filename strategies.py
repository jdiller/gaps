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

        if right_most is not None:
            moveable = tableau.find_moveable_for_gap(right_most)
            tableau.swap(right_most, moveable)
