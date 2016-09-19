from ScrabbleGame import *
from ScrabblePlayer import *
from ScrabbleBot import *
from ScrabbleBotter import *

if __name__ == "__main__":
    sg = ScrabbleGame(BOARD_SIZE)
    weights = [.1, 2.0, -.5, -2, .1, 4.0, 0, .95, 10, 1]
    player1 = ScrabbleBotter(sg.drawTiles(RACK_MAX_SIZE), sg, weights)
    player2 = ScrabbleBotter(sg.drawTiles(RACK_MAX_SIZE), sg, weights)
    sg.playGame(player1, player2)
