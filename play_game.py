from ScrabbleGame import *
from ScrabblePlayer import *
from ScrabbleBot import *

if __name__ == "__main__":
    sg = ScrabbleGame(BOARD_SIZE)
    player1 = ScrabblePlayer(sg.drawTiles(RACK_MAX_SIZE), sg)
    weights = [0.443580677678, -0.00103985979046, -0.256285391028, 0.241350106301, 0.64593861657, 0.295306093895, 0.568277126434, 0.613202356163, 1.15153133191, -0.22725055767, 0.795235582993] #elo weight best
    player2 = ScrabbleBotter(sg.drawTiles(RACK_MAX_SIZE), sg, weights)
    sg.playGame(player1, player2)
