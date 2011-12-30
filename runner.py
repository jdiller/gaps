from game import Game
from datetime import datetime
import curses

stdscr = curses.initscr()
curses.noecho()
stdscr.keypad(1)


wins = 0

try:
    for i in range(1,1001):
        g = Game()
        g.play()
        if g.game_won():
            wins +=1
        stdscr.addstr(0,0,"Wins: %d of %d (%f %%)" % (wins, i, (float(wins) / i * 100)))
        stdscr.refresh()
finally:
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()
print "Wins: %d of %d (%f %%)" % (wins, i, (float(wins) / i * 100))
