##class Game: will store players and winner
##you will append moves
import numpy as np
from os import listdir

class Game:
	def __init__( self, moves ): ##right now everything is stored as a string 
		self.moves = moves
		self.numberMoves = len(moves)

class Move:

	def __init__(self, moveContents): 
		self.player = moveContents[0]
		self.wordBank = moveContents[1]
		self.position = moveContents[2]
		self.wordPlayed = moveContents[3]
		self.pointsGained = moveContents[4]
		self.totalScore = moveContents[5]


def loadDataset(filename="anno24148.gcg"):
    my_data = np.genfromtxt(filename, skip_header=0, dtype=str)
    return my_data

def parseData( my_data ):
	allMoves = []
	for row in my_data:
		moveContents = []
		for x in range(len(row)):
			moveContents.append(row[x])
		currMove = Move(moveContents)
		allMoves.append(currMove)
	return allMoves





##def parseGames(): ##this will loop through all the files and call load dataset in a loop


if __name__=="__main__":
    my_data = loadDataset()
    currGame = Game(parseData(my_data))







