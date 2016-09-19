from ScrabbleGame import *
from ScrabblePlayer import *
from ScrabbleBot import *
from ScrabbleBotter import *

if __name__ == "__main__":
    sg = ScrabbleGame(BOARD_SIZE)
    # weights = [.1, 2.0, -.5, -2, .1, 4.0, 0, .95, 10, 1]
    weights = [0.988508935767, 0.0449722132803, 0.917136969275, 0.906251309118, 0.200199788274, 0.0608824598045, 0.483468715233, 0.299694019611, 0.790554830569, 0.772933371626, 0.146498061342]
    player1 = ScrabbleBot(sg.drawTiles(RACK_MAX_SIZE), sg)
    player2 = ScrabbleBotter(sg.drawTiles(RACK_MAX_SIZE), sg, weights)
    sg.playGame(player1, player2)
