from __future__ import division
import numpy as np;
import twl;
import random;
from copy import deepcopy
from ScrabblePlayer import *
from scrabble_globals import *


# OUR BOT GOES HERE

# self.rack is an instance variable for the bot's current rack of tiles
V_WEIGHT = 3 # lose how many points for each v left in hand
VOWEL_RACK_WEIGHT = 10 #how much is an uneven vowel/consonant ratio on your next turn penalized
POINT_RACK_WEIGHT = 1 #how much are you rewarded for keeping points in your hand

class BoardWord():
    def __init__(self, _letter, _direction, _x, _y):
        self.letter = _letter
        self.direction = _direction
        self.loctation = (_x, _y)

class ScrabbleBot(ScrabblePlayer):

    # Need to return a dictionary of (row, col):letter pairs
    # Input board is a ScrabbleBoard object
    def chooseMove(self, board):
        move = []
        move = self.buildList()
        move = self.checkLegalMoves(move)
        #print move
        #print self.rack
        #if there is no move available, just do nothing
        if self.game.board.isEmpty():
            wordList = twl.anagram(''.join(self.rack))
            for word in wordList:
                defMove = {}
                # print word
                for i in range(len(word)):
                    defMove[(7, 7+i)] = word[i]
                # print defMove
                move.append(defMove)
            # defMove = {}
            # x = 7,7
            # defMove[x] = self.rack[0]
            # return defMove
        if len(move) < 1:
            return move
        move = self.greedyMove(move)
        print self.rackWeight(move)
        return move


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
        return VOWEL_RACK_WEIGHT * rat_flaw

    def pointRackWeight(self, points): #number of points left in hand
        return POINT_RACK_WEIGHT * points

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
                finalWeight -= V_WEIGHT
            pointCount += TILE_POINTS[letter]
        vowelCount += self.vowelProb(move)
        consCount += len(move)-self.vowelProb(move)
        # print self.vowelProb(move), "vowel"
        vcRatio = min(vowelCount, consCount) / max(vowelCount, consCount) # 1 is best
        finalWeight -= self.vowelRackWeight(vcRatio)
        finalWeight += self.pointRackWeight(pointCount)
        return finalWeight
