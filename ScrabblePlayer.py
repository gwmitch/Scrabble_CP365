

# Base player class...defaults to human console control
class ScrabblePlayer:

    def __init__(self, starting_tiles):
        self.rack = starting_tiles

    def receiveScore(self, points):
        print "Just got %d points!" % points

    def chooseMove(self, board):
        move = {}
        print "My current rack:"
        for r in self.rack:
            print r.upper(),
        print
        while True:
            txt = raw_input("Enter row, col, tile: ")
            if txt:
                row, col, tile = txt.split()
                move[int(row), int(col)] = tile
            else:
                break
        return move
