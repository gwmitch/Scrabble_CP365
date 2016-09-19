##class Game: will store players and winner
##you will append moves
import numpy as np
import os, sys
from os import listdir
from ScrabbleGame import *
from ScrabblePlayer import *
from scrabble_globals import *


class LearningModel:

	def __init__(self, games):
		self.games = games

	def initialize(self, allData, dir_num): 
		global total
		count = 0
		for i in range( 1, len(allData) ): ##exclude .DS_Store
			currGame = self.parseSingleGame(allData[i], dir_num)
			if not (currGame is None):
				currGameMoves = self.parseSingleGameToMoves(currGame)
				self.games.append(Game(currGameMoves))
				count += 1
			#else:
			#	count += 1 
		total = total + count
		self.board = [0] * 6489
		#print count
		#print count
		##self.games[0].printGame()

	def parseSingleGame(self, game, dir_num):
		filename = "GameData/" + str(dir_num) + "/" + game
		try:
			my_data = np.genfromtxt(filename, skip_header=2, skip_footer=1, dtype=str)
			return my_data
		except:
			#print "Error with file: " + filename
			return None

	def parseSingleGameToMoves(self, my_data):
		allMoves = []
		for row in my_data:
			moveContents = []
			for x in row:
				for letter in x:
					if letter.islower():
						blank_tile = letter
						x.replace(".", blank_tile)
				moveContents.append(x)
			currMove = Move(moveContents)
			allMoves.append(currMove)
		return allMoves

	#def findStartingDirection(self):
	#	self.first_move = self.games[0]
	#	if self.first_move.position == "H8":
	#		print "Cannot determine direction of starting move."
	#	else:
	#		self.parseMoveLocation(self.first_move)
	#		is_vertical = TestMoveOnBoard.goesThroughCenter()
	#	return is_vertical
      
	def changeLetterToNumber(self, letter):
		letter_num = ord(letter) - 96
		return letter_num

	def parseMoveLocation(self, move):
		col = self.changeLetterToNumber(move.position[0]) - 1
		row = int(move.position[1] + move.position[2]) - 1

		for letter in move.wordPlayed:
			TestMoveOnBoard.move_dictionary[(row, col)]= str(letter)
			self.addMoveToList(move, row, col)

	def addMoveToList(self, move, row, col):
		is_vertical = TestMoveOnBoard.isMoveVertical()
		for letter in move.wordPlayed:
			list_position = (row * 405) + col + self.changeLetterToNumber(letter)
			self.board[list_position] = 1
			if is_vertical == true:
				col += 1
			else:
				row += 1

	def parseWordBank(self, move):
		slot = 0
		for letter in move.wordBank:
			list_position = 6075 + self.changeLetterToNumber(letter) + slot
			self.board[list_position] = 1
			slot += 27

	def parseMoves(self):
		for move in self.games:
			self.parseMoveLocation(move)
			self.parseWordBank(move)


	def printBoard(self):
		print self.board

class Game:

	def __init__( self, moves ): #right now everything is stored as a string 
		self.moves = moves
		self.numberMoves = len(moves)

	def printGame(self):
		for i in range(len(self.moves)):
			print "move: "
			self.moves[i].printMove()

class TestMoveOnBoard(ScrabblePlayer):
	
	def inputMove(self):
		self.move_dictionary = {}
		#moves = []
		for key, move in self.move_dictionary.iteritems():
			if(self.game.boardWouldBeLegal(move)):
				return move

	def isMoveVertical(self):
		if self.move_dictionary.keys()[1][0] != self.move_dictionary.keys()[0][0]:
			return true
		return false

  	def goesThroughCenter(self):
  		move = self.inputMove()
  		if (7,7) in self.move_dictionary.keys():
  			return true
  		return false


class Move:

	def __init__(self, moveContents): 
		self.player = moveContents[0]
		self.wordBank = moveContents[1]
		self.position = moveContents[2]
		self.wordPlayed = moveContents[3]
		self.pointsGained = moveContents[4]
		self.totalScore = moveContents[5]

		#self.board = [0] * 6489

	#def initializeBoard(self):
		#self.board = [0 for col in range(405)] for row in range(15)]
		#self.board = [0] * 6489

	#def printMoveBoard(self):
	#	print self.board

	#def printMove(self):
	#	moveString = "Player: " + self.player + " WordBank: " + self.wordBank + " Position: " + self.position + " WordPlayed: " + self.wordPlayed + " PointsGained: " + self.pointsGained + " TotalScore: " + self.totalScore
	#	print moveString

	
	#def findMoveDirection(self):
	#	TestMoveOnBoard
	#	return is_vertical

def loadAllDataSets(dir_num):
	games = os.listdir("GameData/" + str(dir_num) + "/")
	return games



if __name__=="__main__":

    ##my_data = loadSingleDataset()
    ##currGame = Game(parseData(my_data))
	global total
	total = 0
	for i in range(0, 246):
		games = loadAllDataSets(i)
		emptyArr = []
		model = LearningModel(emptyArr)
		model.initialize(games, i)
	print total
	model.parseMoves()
	model.printBoard()