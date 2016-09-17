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

    def exchangeTiles(self, to_replace):
        for tile in to_replace:
            self.rack.remove(tile)
        number_to_pick = RACK_MAX_SIZE - len(self.rack)
        self.rack += self.game.drawTiles(number_to_pick)

    def chooseMove(self, board):
        print "My current rack:"
        for r in self.rack:
            print r.upper(),
        print
        while True:
            txt = raw_input("Enter row, column, (direction,) word: ")
            if txt:
                tokens = txt.split()
                print txt
                if len(tokens) == 4:
                    row, col, direction, word = tokens
                elif len(tokens) == 3:
                    row, col, word = tokens
                    direction = "h"
                elif len(tokens) == 2 and tokens[0].lower() == "exchange":
                    print "Exchanging ", tokens[1]
                    self.exchangeTiles(tokens[1])
                    return {}  # have to pass when exchanging
                else:
                    print "wrong input"
                    return {}
                row = int(row)
                col = int(col)
                move = {}
                for c in word:
                    while self.game.board.getTile(row,col) != " ":
                        if direction == "v":
                            row += 1
                        else:
                            col += 1
                    move[int(row), int(col)] = c
                    if direction == "v":
                        row += 1
                    else:
                        col += 1
                if(self.game.boardWouldBeLegal(move)):
                    return move
            else:
                return {}
