from __future__ import division
import numpy as np;
import twl;
import random;
from copy import deepcopy
from ScrabblePlayer import *
from scrabble_globals import *

# self.rack is an instance variable for the bot's current rack of tiles

class BoardWord():
    def __init__(self, _letter, _direction, _x, _y):
        self.letter = _letter
        self.direction = _direction
        self.loctation = (_x, _y)

class ScrabbleBotter(ScrabblePlayer):

    def __init__(self, starting_tiles, game, weights):
        self.rack = starting_tiles
        self.game = game
        self.LETTER_MULTS_GOT_W = weights[0]
        self.WORD_MULTS_GOT_W = weights[1]
        self.LETTER_MULTS_OPENED_W = weights[2]
        self.WORD_MULTS_OPENED_W = weights[3]
        self.SPACES_OPENED_W = weights[4]
        self.TILE_VALUE_W = weights[5] #Most important one, it seems
        self.RACK_QUALITY_W = weights[6]
        self.V_WEIGHT = weights[7]
        self.VOWEL_RACK_WEIGHT = weights[8]
        self.POINT_RACK_WEIGHT = weights[9]
    # Need to return a dictionary of (row, col):letter pairs
    # Input board is a ScrabbleBoard object
    def chooseMove(self, board):
        moves = []
        moves = self.buildList()
        moves = self.checkLegalMoves(moves)
        #print move
        #print self.rack

        #if there is no move available, just do nothing
        if len(moves) < 1:
            defMove = {}
            x = 7,7
            defMove[x] = self.rack[0]
            return defMove

        return self.smartMove(moves)

    def buildList(self):
        moveList = []

        for i in range(0, BOARD_SIZE):
            currentMove  = {}
            currentBW = BoardWord(''.join(self.game.board.board[:,i].tolist()), True, i, 0)
            wordList = self.anagram(currentBW, self.rack)
            for item in wordList:
                currentMove = {}
                offset,word = item
                for j in range(offset, (offset+ len(word))):
                        if word[j - offset] not in currentBW.letter[j]:
                            currentMove[j, i] = word[j - offset]
                moveList.append(currentMove)
                # print moveList

        for k in range(0, BOARD_SIZE):
            currentMove = {}
            currentBW = BoardWord(''.join(self.game.board.board[k,:].tolist()), False, i, 0)
            wordList = self.anagram(currentBW, self.rack)
            for item in wordList:
                currentMove = {}
                offset,word = item
                for j in range(offset, (offset+ len(word))):
                        if word[j - offset] not in currentBW.letter[j]:
                            currentMove[k, j] = word[j - offset]
                moveList.append(currentMove)

        return moveList

    def checkLegalMoves(self, moves):
        finalMoves = []
        for move in moves:
            if(self.game.boardWouldBeLegal(move)):
                finalMoves.append(move)
                #print move
        return finalMoves

    def evaluate_word(self, word, index, spaces_before, letters,hand):
        original_hand_size = len(hand)
        # explained later in the code
        letters_search = letters + " "

        offset = spaces_before - index
        if offset < 0:
            return -1
        if offset != 0 and letters[offset-1] != ' ':
            return -1
        else:
            words_match = True
            if offset + len(word) > len(letters):
                return -1
            for i in range(0, len(word)):
                offset_i = i + offset
                if letters[offset_i] != ' ':
                    if letters[offset_i] != word[i]:
                        words_match = False
                        break
                else:

                    if not word[i] in hand:
                        return -1
                    else:
                        letter_index = hand.index(word[i])
                        hand = hand[:letter_index] + hand[letter_index+1:]
            if words_match:
                # check if any letter from hand has been used
                if len(hand) >= original_hand_size:
                    return -1
                # previously we appended a space to the letters on board, so that we don't run into
                # a non-existing index issue
                if letters_search[offset+len(word)] == ' ':
                    return offset
        return -1

    def anagram(self, boardword, hand):
        letters = boardword.letter
        cleanstring = letters.strip()
        combo = cleanstring.join(hand)
        combinations = list(twl.anagram(combo))

        possible_words = []

        for i in range(len(letters)):
            if letters[i] != ' ':
                spaces_before = i
                letter = letters[i]

                for word in combinations:
                    letter_occurrences = [index for index, char in enumerate(word) if char == letter]
                    for index in letter_occurrences:
                        offset = self.evaluate_word(word, index, spaces_before, letters, hand)
                        if (offset > -1):
                            possible_words.append((offset, word ))

        return list(set(possible_words))

    def bigMove(self, moves):
        high = 0
        for move in moves:
            if len(move) > high:
                high = len(move)
                finalMove = move
        return finalMove

    def greedyMove(self, moves):
        high = 0
        for move in moves:
            self.game.performMove(move)
            if self.game.scoreMove(move) > high:
                print high
                high = self.game.scoreMove(move)
                finalMove = move
            self.game.undoMove(move)
        return finalMove



    #Returns the straightforward point value of a word
    #Avg range 1-200
    def pointVal(self, move):
        self.game.performMove(move)
        value = self.game.scoreMove(move)
        self.game.undoMove(move)
        return value

    #Returns the sum of the word multipliers that a move will get
    #IE a move that hits a triple and a double will return 5
    #Avg range 0-6
    def wordMultsGot(self, move):
        total = 0
        for key in move:
            if BOARD_WORD_MULTIPLIERS.has_key(key):
                total += BOARD_WORD_MULTIPLIERS[key]**2
        return total

    #Returns the sum of the letter multipliers that a move will get
    #IE a move that hits a triple and a double will return 5
    #Avg range 0-6
    def letterMultsGot(self, move):
        total = 0
        for key in move:
            if BOARD_LETTER_MULTIPLIERS.has_key(key):
                total += BOARD_LETTER_MULTIPLIERS[key]**2
        return total

    #Returns true if all cardinally adjacent spaces are empty
    #false otherwise
    def emptyAdjacent(self, row, col):
        b = self.game.board
        if (row > 0 and b.getTile(row-1,col) != ' ') or (row < BOARD_SIZE-1 and b.getTile(row+1,col) != ' ') or (col > 0 and b.getTile(row, col-1) != ' ') or (col<BOARD_SIZE-1 and b.getTile(row, col+1) != ' '):
            return False
        else: return True

    #Returns the sum of spaces opened, letter multipliers opened, and weight multipliers opened, each weighted by their respective weights
    def boardOpened(self, move):
        b = self.game.board

        spacesOpened = 0
        wordMultsOpened = 0
        letterMultsOpened = 0

        for key in move:
            #Cast east
            row, col = key
            row+=1
            while(row < BOARD_SIZE and b.getTile(row, col) == ' ' and self.emptyAdjacent(row, col)):
                newKey = row, col
                spacesOpened +=1
                if BOARD_WORD_MULTIPLIERS.has_key(newKey): wordMultsOpened += BOARD_WORD_MULTIPLIERS[newKey]**2 * 1.0 / abs(row-key[0])
                elif BOARD_LETTER_MULTIPLIERS.has_key(newKey): letterMultsOpened += BOARD_LETTER_MULTIPLIERS[newKey]**2 * 1.0 / abs(row-key[0])
                row +=1

            #Cast west
            row, col = key
            row-=1
            while(row >=0 and b.getTile(row, col) == ' ' and self.emptyAdjacent(row, col)):
                newKey = row, col
                spacesOpened +=1
                if BOARD_WORD_MULTIPLIERS.has_key(newKey): wordMultsOpened += BOARD_WORD_MULTIPLIERS[newKey]**2 * 1.0 / abs(row-key[0])
                elif BOARD_LETTER_MULTIPLIERS.has_key(newKey): letterMultsOpened += BOARD_LETTER_MULTIPLIERS[newKey]**2 * 1.0 / abs(row-key[0])
                row -=1

            #Cast north
            row, col = key
            col -= 1
            while(col >= 0 and b.getTile(row, col) == ' ' and self.emptyAdjacent(row, col)):
                newKey = row, col
                spacesOpened +=1
                if BOARD_WORD_MULTIPLIERS.has_key(newKey): wordMultsOpened += BOARD_WORD_MULTIPLIERS[newKey]**2 * 1.0/ abs(col-key[1])
                elif BOARD_LETTER_MULTIPLIERS.has_key(newKey): letterMultsOpened += BOARD_LETTER_MULTIPLIERS[newKey]**2 * 1.0 / abs(col-key[1])
                col -=1

            #Cast south
            row, col = key
            col+=1
            while(col < BOARD_SIZE and b.getTile(row, col) == ' ' and self.emptyAdjacent(row, col)):
                newKey = row, col
                spacesOpened +=1
                if BOARD_WORD_MULTIPLIERS.has_key(newKey): wordMultsOpened += BOARD_WORD_MULTIPLIERS[newKey]**2 * 1.0 / abs(col-key[1])
                elif BOARD_LETTER_MULTIPLIERS.has_key(newKey): letterMultsOpened += BOARD_LETTER_MULTIPLIERS[newKey]**2 * 1.0 / abs(col-key[1])
                col +=1

        returnVal = (spacesOpened * self.SPACES_OPENED_W) + (wordMultsOpened * self.WORD_MULTS_OPENED_W) + (letterMultsOpened * self.LETTER_MULTS_OPENED_W)
        return returnVal

    #Returns the "value" of the tiles being played
    #A pretty nebulous idea, but seems to help a lot
    #Tries to ensure that if high value tiles are being played, they're getting multipliers
    #Currently sets the "desired" value of any tile as triple the default value
    def tileValue(self, move):
        relativeValue = 0
        multiVal = 1
        for key in move:
            if BOARD_WORD_MULTIPLIERS.has_key(key): multiVal = multiVal * BOARD_WORD_MULTIPLIERS[key]
        for key, val in move.items():
            letterVal = TILE_POINTS[val]
            desiredVal = letterVal*3
            letterMultVal = 1
            if BOARD_LETTER_MULTIPLIERS.has_key(key): letterMultVal = BOARD_LETTER_MULTIPLIERS[key]
            actualVal = letterVal * multiVal * letterMultVal
            relativeValue += actualVal - desiredVal
        return relativeValue

    def vowelProb(self, move):
        board = list(self.game.board.board.flatten().tostring())
        letters = list((self.game.tile_distribution))
        vowelCount  = 0
        # print letters
        for letter in letters:
            if letter in board:
                board.remove(letter)
                letters.remove(letter)
        # print letters
        for letter in letters:
            if letter in list("aeiou"):
                vowelCount += 1
        vowelRatio = vowelCount/len(letters)
        # print vowelCount, len(letters), vowelCount/len(letters), "ratio"
        return vowelRatio * len(move)

    def vowelRackWeight(self, ratio): #ratio of vowels to consonants in next hand
        IDEAL_RATIO = 1
        rat_flaw = IDEAL_RATIO - ratio
        return self.VOWEL_RACK_WEIGHT * rat_flaw

    def pointRackWeight(self, points): #number of points left in hand
        return self.POINT_RACK_WEIGHT * points

    def rackWeight(self, move):
        finalWeight = 0
        tempRack = deepcopy(self.rack)
        vowelCount = 0
        consCount = 0
        pointCount = 0
        for key, value in move:
            tempRack.remove(move[(key,value)])
        for letter in tempRack:
            if letter in "aeiou":
                vowelCount += 1
            else:
                consCount += 1
            if letter == "v":
                finalWeight -= self.V_WEIGHT
            pointCount += TILE_POINTS[letter]
        vowelCount += self.vowelProb(move)
        consCount += len(move)-self.vowelProb(move)
        # print self.vowelProb(move), "vowel"
        #edited here to include division
        vcRatio = min(vowelCount, consCount)/max(vowelCount, consCount) # 1 is best
        finalWeight -= self.vowelRackWeight(vcRatio)
        finalWeight += self.pointRackWeight(pointCount)
        return finalWeight
    #Returns a value for a move based on the point value AND all heuristics
    def getValue(self, move):
        value = 0
        value += self.pointVal(move)**1.5
        value += self.boardOpened(move)
        value += self.letterMultsGot(move) * self.LETTER_MULTS_GOT_W
        value += self.wordMultsGot(move) * self.WORD_MULTS_GOT_W
        value += self.tileValue(move) * self.TILE_VALUE_W
        value += self.rackWeight(move) * self.RACK_QUALITY_W
        return value

    def smartMove(self, moves):
        highPointVal = 0
        high = self.getValue(moves[0])
        finalMove = moves[0]
        del moves[0]
        for move in moves:
            value = self.getValue(move)
            pv = self.pointVal(move)
            if pv > highPointVal: highPointVal = pv
            if value > high:
                high = value
                finalMove = move

        print "Highest possible pv: %s" % highPointVal
        print "Value: %s" % high
        return finalMove