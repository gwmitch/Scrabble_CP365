

# Base player class...defaults to human console control
class ScrabblePlayer:

    def __init__(self, starting_tiles):
        self.rack = starting_tiles

    def receiveScore(self, points):
        print "Just got %d points!" % points

    def hasTiles(self, move):
        rack_copy = self.rack[:]
        for m in move.values():
            if m not in rack_copy:
                return False
            else:
                rack_copy.remove(m)
        return True

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
