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
            for j in range(pop_size-1):
                sGame = ScrabbleGame(BOARD_SIZE)
                p2 = (p1+j)%pop_size
                bot1 = ScrabbleBotter(sGame.drawTiles(RACK_MAX_SIZE), sGame, self.bots[p1])
                bot2 = ScrabbleBotter(sGame.drawTiles(RACK_MAX_SIZE), sGame, self.bots[p2])
                sg = sGame.playGame(bot1, bot2)
                scores[p1] += sg[0] - sg[1]
                scores[p2] += sg[1] - sg[0]
                print "score ", scores

        print "scores ", scores
        for ind in scores:
            self.fitnesses[ind] = scores[ind] * 1/len(self.bots)
            print ind, scores[ind], self.fitnesses[ind]

    def generateRandomSolution(self):
        s = []
        for i in range(length):
            s.append(random.uniform(0,1))
        return s

    def generateInitPopulation(self, pop_size):
        for i in range(pop_size):
            self.bots.append(self.generateRandomSolution())
        self.generatePopulationFitness()


    def pickFitParent(self):
        self.fitnesses += (min(self.fitnesses)) + 1 #pushing them all above 0
        total_fitnesses = sum(self.fitnesses)
        r = random.randrange(total_fitnesses)
        ind = -1
        while r > 0:
            ind += 1
            r -= self.fitnesses[ind]
        return self.bots[ind]

    def pickBestN(self, n):
        bestGenomes = []
        for i in range(n):
            max_value = max(self.fitnesses)
            max_index = self.fitnesses.index(max_value)
            bestGenomes.append(self.bots.pop(max_index)) #remove best from population
            self.bots_fitnesses.pop(max_index)   #remove best from fitnesses
        return bestGenomes

    def crossover(self, p1, p2):
        baby = []
        for i in range(len(p1)):
            baby.append(random.choice(p1[i],p2[i]))
        return baby

    def mutate(self, child, mutation_rate):
        new_child = []
        for weight in child:
            if random.random() < mutation_rate:
                weight = np.random.normal(weight, weight*.15)
        return new_child

    def getBestSolution(self):
        max_ind = self.bots_fitnesses.index(max(self.bots_fitnesses))
        return self.bots[max_ind]

    def generateNewPopulation(self, mutation, survival=5):
        new_pop = []
        i = 0
        while i < len(self.bots)-survival:
            p1 = self.pickFitParent()
            p2 = self.pickFitParent()
            child = self.crossover(p1, p2)
            child = self.mutate(child, mutation)
            new_pop.append(child)
        new_pop.append(self.pickBestN(survival))
        self.bots = new_pop

    def evolve(self, number_epochs, mutation = .01, min_mutation = .001, shrink = .95):
        self.generateInitPopulation(10)
        print("self.fitnesses: ", self.fitnesses)
        for i in range(number_epochs):
            self.generateNewPopulation(mutation)
            self.generatePopulationFitnesses()
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
