from game import Game
from datetime import datetime
from optparse import OptionParser
import curses

stdscr = curses.initscr()
curses.noecho()
stdscr.keypad(1)

started = datetime.now()
wins = 0

parser = OptionParser()
parser.add_option("-r", "--repeat", dest="repeats",
        help="Number of games to run", default="1000")

parser.add_option("-s", "--strategy", dest="strategy",
        help="Strategy to use")

(options, args) = parser.parse_args()

repeats = int(options.repeats) + 1
try:
    for i in range(1,repeats):
        g = Game(options.strategy)
        g.play()
        if g.game_won():
            wins +=1
        now = datetime.now()
        elapsed = now - started
        seconds = elapsed.total_seconds()
        hands_per_second = float(i) / seconds
        stdscr.addstr(0,0,"%s - Wins: %d of %d (%f %%) - %f games/s" % \
                (options.strategy, wins, i, (float(wins) / i * 100), hands_per_second))
        stdscr.refresh()
finally:
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()
print "%s - Wins: %d of %d (%f %%) - %f games/s" % (options.strategy, wins, i, (float(wins) / i *100),hands_per_second)
