from ScrabbleGame import *
from ScrabblePlayer import *
from ScrabbleBot import *
from ScrabbleBotter import *

if __name__ == "__main__":
    sg = ScrabbleGame(BOARD_SIZE)
    #weights = [.1, 1, -.5, -2, .1, 4.0, 0, .95, 1, 1]
    #weightsp2 = [0.434552526983, 0.0695333713975, -0.244925612275, 0.151061392263, 0.504794041753, 0.468776347428, 0.644338989372, 0.54300419617, 1.18654167414, -0.246213177556, 0.769765798309] #aidan best generation 5
    weights = [0.443580677678, -0.00103985979046, -0.256285391028, 0.241350106301, 0.64593861657, 0.295306093895, 0.568277126434, 0.613202356163, 1.15153133191, -0.22725055767, 0.795235582993] #generation 6 best
    player1 = ScrabbleBot(sg.drawTiles(RACK_MAX_SIZE), sg)
    player2 = ScrabbleBotter(sg.drawTiles(RACK_MAX_SIZE), sg, weights)
    sg.playGame(player1, player2)
