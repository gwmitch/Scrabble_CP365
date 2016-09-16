##class Game: will store players and winner
##you will append moves
import numpy as np
import os, sys
from os import listdir


class LearningModel:
	def __init__(self, games):
		self.games = games

	def initialize(self, allData): 
		count = 0
		for i in range( 1, len(allData) ): ##exclude .DS_Store
			currGame = self.parseSingleGame(allData[i])
			if not (currGame is None):
				currGameMoves = self.parseSingleGameToMoves(currGame)
				self.games.append(Game(currGameMoves))

		#print count
		##self.games[0].printGame()

	def parseSingleGame(self, game):
		filename = "LearningData/" + game
		try:
			my_data = np.genfromtxt(filename, skip_header=0, dtype=str)
			print filename
			return my_data
		except:
			print "Error with file: " + filename

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

def loadAllDataSets():
	allGames = os.listdir("LearningData/")
	return allGames


if __name__=="__main__":
    ##my_data = loadSingleDataset()
    ##currGame = Game(parseData(my_data))
    allGames = loadAllDataSets()
    emptyArr = []
    model = LearningModel(emptyArr)
    model.initialize(allGames)
    print model.games[0].moves[0].wordPlayed.lower()
