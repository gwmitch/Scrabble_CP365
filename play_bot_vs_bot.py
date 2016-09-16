from ScrabbleGame import *
from ScrabblePlayer import *
from ScrabbleBot import *

if __name__ == "__main__":
    sg = ScrabbleGame(BOARD_SIZE)
    player1 = ScrabbleBot(sg.drawTiles(RACK_MAX_SIZE), sg)
    player2 = ScrabbleBot(sg.drawTiles(RACK_MAX_SIZE), sg)
    sg.playGame(player1, player2)
