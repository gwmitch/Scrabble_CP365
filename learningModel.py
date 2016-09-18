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
<<<<<<< HEAD
				count += 1
			#else:
			#	count += 1 
		total = total + count
		print count
		#print total
=======

		#print count
>>>>>>> b7c9ac969256d03e96d8fb0ca1d28452ca07cbac
		##self.games[0].printGame()

	def parseSingleGame(self, game, dir_num):
		filename = "GameData/" + str(dir_num) + "/" + game
		try:
<<<<<<< HEAD
			my_data = np.genfromtxt(filename, skip_header=2, skip_footer=1, dtype=str)
			return my_data
		except:
			#print "Error with file: " + filename
=======
			my_data = np.genfromtxt(filename, skip_header=0, dtype=str)
			print filename
			return my_data
		except:
			print "Error with file: " + filename

>>>>>>> b7c9ac969256d03e96d8fb0ca1d28452ca07cbac
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

<<<<<<< HEAD





def loadAllDataSets(dir_num):
	games = os.listdir("GameData/" + str(dir_num) + "/")
	return games
=======
def loadAllDataSets():
	allGames = os.listdir("LearningData/")
	return allGames
>>>>>>> b7c9ac969256d03e96d8fb0ca1d28452ca07cbac


if __name__=="__main__":
    ##my_data = loadSingleDataset()
    ##currGame = Game(parseData(my_data))
<<<<<<< HEAD
	global total
	total = 0
	for i in range(0, 246):
		games = loadAllDataSets(i)
		emptyArr = []
		model = LearningModel(emptyArr)
		model.initialize(games, i)
	print total
=======
    allGames = loadAllDataSets()
    emptyArr = []
    model = LearningModel(emptyArr)
    model.initialize(allGames)
    print model.games[0].moves[0].wordPlayed.lower()
>>>>>>> b7c9ac969256d03e96d8fb0ca1d28452ca07cbac
