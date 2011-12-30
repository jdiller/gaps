class MoveLeftMostMoveable(object):
    #always finds and moves left-most card that can be moved
    def apply_strategy(self, tableau):
        moveables = tableau.find_moveable()
        left_most = None
        for m in moveables:
            if left_most is None or left_most[1] > m[1]:
                left_most = m
        gap = tableau.find_gap_for_moveable(m)
        tableau.swap(m, gap)


