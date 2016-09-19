from ScrabbleGame import *
from ScrabblePlayer import *
from ScrabbleBot import *
from ScrabbleBotter import *

if __name__ == "__main__":
    sg = ScrabbleGame(BOARD_SIZE)
    #weights = [.1, 1, -.5, -2, .1, 4.0, 0, .95, 1, 1]
    #weightsp2 = [0.434552526983, 0.0695333713975, -0.244925612275, 0.151061392263, 0.504794041753, 0.468776347428, 0.644338989372, 0.54300419617, 1.18654167414, -0.246213177556, 0.769765798309] #aidan best generation 5
    weightsp1 = [0.358398670334, -0.0258820809337, -0.0117747523405, -0.048199454868, 0.144839908045, 0.0998114509692, 0.68054231695, 0.64982813339, 0.921265680606, -0.102322611715, 0.732581560706] #generation 6 best
    player1 = ScrabbleBotter(sg.drawTiles(RACK_MAX_SIZE), sg, weightsp1)
    player2 = ScrabbleBotter(sg.drawTiles(RACK_MAX_SIZE), sg, weightsp1)
    sg.playGame(player1, player2)
