from __future__ import division
import random
import random
import string
import io
import numpy as np
from ScrabbleBot import *
from ScrabbleGame import *
from ScrabblePlayer import *
from scrabble_globals import *
from ScrabbleBotter import *

length = 10 #length of genes

class GA:
    def __init__(self):
        self.bots = [] #list of genes? (doubles)
        #self.weights = []
        self.fitnesses = []

    def generatePopulationFitness(self):
        pop_size = len(self.bots)
        print "GENERATING POPULATION FITNESS"
        scores = []
        mybots = []
        for i in range(pop_size): scores.append(0) #initializes list
        for p1 in range(pop_size):
            for j in range(1, pop_size):
                sGame = ScrabbleGame(BOARD_SIZE)
                # print p1
                p2 = (p1+j)%pop_size
                # print p2
                # print self.bots
                bot1 = ScrabbleBotter(sGame.drawTiles(RACK_MAX_SIZE), sGame, self.bots[p1])
                bot2 = ScrabbleBotter(sGame.drawTiles(RACK_MAX_SIZE), sGame, self.bots[p2])
                sg = sGame.playGame(bot1, bot2)
                # print sg[0], sg[1]
                # print sg[0] - sg[1]
                # print scores[p1] + (sg[0] - sg[1])
                scores[p1] = scores[p1] + (sg[0] - sg[1])
                scores[p2] += sg[1] - sg[0]
                # print "score ", scores

        # print "scores ", scores
        for ind in range(len(scores)):
            print ind
            print self.fitnesses
            print scores
            self.fitnesses[ind] = scores[ind] * 1/pop_size
            print ind, scores[ind], self.fitnesses[ind]

    def generateRandomSolution(self):
        s = []
        for i in range(length):
            s.append(random.uniform(0,1))
        return s

    def generateInitPopulation(self, pop_size):
        for i in range(pop_size):
            self.fitnesses.append(0)
            self.bots.append(self.generateRandomSolution())
        self.generatePopulationFitness()


    def pickFitParent(self):
        # print self.fitnesses
        for i in range(len(self.fitnesses)):
            self.fitnesses[i] += (abs(min(self.fitnesses)) + 1) #pushing them all above 0
        total_fitnesses = sum(self.fitnesses)
        # print self.fitnesses
        r = random.randrange(total_fitnesses)
        ind = -1
        while r > 0:
            ind += 1
            r -= self.fitnesses[ind]
        return self.bots[ind]

    def pickBestN(self, n):
        bestGenomes = []
        for i in range(n):
            # print "?"
            print self.fitnesses
            max_value = max(self.fitnesses)
            max_index = self.fitnesses.index(max_value)
            # print max_index, "max index"
            print self.bots[max_index]
            bestGenomes.append(self.bots.pop(max_index)) #remove best from population
            self.bots.append(0)
            self.fitnesses.pop(max_index)   #remove best from fitnesses
            self.fitnesses.append(0)
        return bestGenomes

    def crossover(self, p1, p2):
        baby = []
        for i in range(len(p1)):
            baby.append(random.choice((p1[i],p2[i])))
        # print baby, "baby"
        return baby

    def mutate(self, child, mutation_rate):
        for weight in child:
            if random.random() < mutation_rate:
                weight = np.random.normal(weight, weight*.15)
        return child

    def getBestSolution(self):
        max_ind = self.bots_fitnesses.index(max(self.bots_fitnesses))
        return self.bots[max_ind]

    def generateNewPopulation(self, mutation, survival=1):
        new_pop = []
        i = 0
        while i < len(self.bots)-survival:
            # print "?"
            p1 = self.pickFitParent()
            p2 = self.pickFitParent()
            child = self.crossover(p1, p2)
            # print "??"
            # print child
            child = self.mutate(child, mutation)
            # print child
            new_pop.append(child)
            i += 1
        # print new_pop, "!"
        bestN = self.pickBestN(survival)
        # print bestN, "?!"
        for item in bestN:
            new_pop.append(item)
        # print new_pop, "!!"
        self.bots = new_pop

    def evolve(self, number_epochs, mutation = .01, min_mutation = .001, shrink = .95):
        self.generateInitPopulation(2)
        print("self.fitnesses: ", self.fitnesses)
        for i in range(number_epochs):
            self.generateNewPopulation(mutation)
            self.generatePopulationFitness()
            if mutation > min_mutation:
                mutation *= shrink
        try:
            open("weights.txt", "w").write("Weights: {0}")
        except:
            print("could not open")
            sys.exit(0)


if __name__=="__main__":
    ga = GA()
    ga.evolve(100000)



























    #
