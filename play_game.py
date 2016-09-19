from ScrabbleGame import *
from ScrabblePlayer import *
from ScrabbleBot import *
from ScrabbleBotter import *

if __name__ == "__main__":
    sg = ScrabbleGame(BOARD_SIZE)
    player1 = ScrabblePlayer(sg.drawTiles(RACK_MAX_SIZE), sg)
    weights = [0.434552526983, 0.0695333713975, -0.244925612275, 0.151061392263, 0.504794041753, 0.468776347428, 0.644338989372, 0.54300419617, 1.18654167414, -0.246213177556, 0.769765798309] #elo weight best
    player2 = ScrabbleBotter(sg.drawTiles(RACK_MAX_SIZE), sg, weights)
    sg.playGame(player1, player2)
