from scrabble_globals import *

# Base player class...defaults to human console control
class ScrabblePlayer:

    def __init__(self, starting_tiles, game):
        self.rack = starting_tiles
        self.game = game

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

    def updateRack(self, previous_move):
        for tile in previous_move.values():
            self.rack.remove(tile)
        number_to_pick = RACK_MAX_SIZE - len(self.rack)
        self.rack += self.game.drawTiles(number_to_pick)

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
                move[int(row), int(col)] = tile.lower()
            else:
                break
        return move
