##class Game: will store players and winner
##you will append moves
import numpy as np
import os, sys
from os import listdir

global total


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
		#print count
		#print total
		##self.games[0].printGame()

	def parseSingleGame(self, game, dir_num):
		filename = "LearningData/" + str(dir_num) + "/" + game
		try:
			my_data = np.genfromtxt(filename, skip_header=2, skip_footer=1, dtype=str)
			return my_data
		except:
			#print "Error with file: " + filename
			return None

	def parseSingleGameToMoves(self, my_data ):
		allMoves = []
		for row in my_data:
			moveContents = []
			for x in range(len(row)):
				moveContents.append(row[x])
			currMove = Move(moveContents)
			allMoves.append(currMove)
		return allMoves

class Game:
	def __init__( self, moves ): ##right now everything is stored as a string 
		self.moves = moves
		self.numberMoves = len(moves)

	def printGame(self):
		for i in range(len(self.moves)):
			print "move: "
			self.moves[i].printMove()

class Move:

	def __init__(self, moveContents): 
		self.player = moveContents[0]
		self.wordBank = moveContents[1]
		self.position = moveContents[2]
		self.wordPlayed = moveContents[3]
		self.pointsGained = moveContents[4]
		self.totalScore = moveContents[5]

	def printMove(self):
		moveString = "Player: " + self.player + " WordBank: " + self.wordBank + " Position: " + self.position + " WordPlayed: " + self.wordPlayed + " PointsGained: " + self.pointsGained + " TotalScore: " + self.totalScore
		print moveString






def loadAllDataSets(dir_num):
	games = os.listdir("LearningData/" + str(dir_num) + "/")
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
	#print total