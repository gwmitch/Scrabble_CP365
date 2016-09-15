import numpy as np;
import twl;
from ScrabblePlayer import *
from scrabble_globals import *


# OUR BOT GOES HERE

# self.rack is an instance variable for the bot's current rack of tiles

class BoardWord():
    def __init__(self, _letter, _direction, _x, _y):
        self.letter = _letter
        self.direction = _direction
        self.loctation = (_x, _y)

class ScrabbleBot(ScrabblePlayer):

    # Need to return a dictionary of (row, col):letter pairs
    # Input board is a ScrabbleBoard object
    def chooseMove(self, board):
        move = {}
        move = self.buildList()
        move = self.checkLegalMoves(move)
        print move[0]
        print self.rack
        return move[0]


    def buildList(self):
        moveList = []

        for i in range(0, BOARD_SIZE):
            currentMove = {}
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
            currentBW = BoardWord(''.join(self.game.board.board[:,i].tolist()), False, i, 0)
            wordList = self.anagram(currentBW, self.rack)
            for item in wordList:
                currentMove = {}
                offset,word = item
                for j in range(offset, (offset+ len(word))):
                        if word[j - offset] not in currentBW.letter[j]:
                            currentMove[i, j] = word[j - offset]
                moveList.append(currentMove)

        return moveList

    def checkLegalMoves(self, moves):
        finalMoves = []
        for move in moves:
            if(self.game.boardWouldBeLegal(move)):
                finalMoves.append(move)
                # print move
        return finalMoves


    def evaluate_word(self, word, index, spaces_before, letters):
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
            if words_match:
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
                        offset = self.evaluate_word(word, index, spaces_before, letters)
                        if (offset > -1):
                            possible_words.append((offset, word ))

        return possible_words
