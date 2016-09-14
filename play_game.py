from ScrabbleGame import *
from ScrabblePlayer import *
from ScrabbleBot import *

if __name__ == "__main__":
    sg = ScrabbleGame(BOARD_SIZE)
    player1 = ScrabblePlayer(sg.drawInitialTiles())
    player2 = ScrabbleBot(sg.drawInitialTiles())

    p1turn = True
    if VISUALIZE:
        sg.visualizeBoard()

    scores = {"player1":0, "player2":0}

    while True:
        print sg.board
        # print "BOARD VALUE:", sg.getBoardValue()
        print scores
        if VISUALIZE:
            sg.visualizeBoard()
        if p1turn:
            curr_player = player1
        else:
            curr_player = player2

        m = curr_player.chooseMove(sg.board)
        if len(m) > 0:
            if sg.isLegalMove(m):
                print m
                points = sg.finalMove(m)
                print "SCORE %d POINTS" % points
                curr_player.receiveScore(points)
                if p1turn:
                    scores['player1'] += points
                else:
                    scores['player2'] += points
        else:
            print "PLAYER PASSED"

        p1turn = not p1turn






















#
