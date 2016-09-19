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

length = 10

class GA:
    def __init__(self):
        self.bots = [] #scores (doubles)
        self.weights = []
        self.sGame = ScrabbleGame(BOARD_SIZE)
        self.fitness = []

    def generatePopulationFitness(self):
        for i in range(length): self.bots.append(ScrabbleBotter(self.sGame.drawTiles(RACK_MAX_SIZE), self.sGame, self.bots[p1], self.weights))
        scores = []
        for i in range(len(scores)): scores.append(0)
        for p1 in range(len(self.bots)):
            for j in len(self.bots)-1:
                p2 = (i+j)%len(self.bots)
            bot1 = ScrabbleBotter(self.sGame.drawTiles(RACK_MAX_SIZE), self.sGame, self.bots[p1], self.weights)
            bot2 = ScrabbleBotter(self.sGame.drawTiles(RACK_MAX_SIZE), self.sGame, self.bots[p2], self.weights)
            sg = self.sGame.playGame(bot1, bot2)
            if i in scores:
                scores[i] += sg[0] - sg[1]
            if p2 in scores:
                scores[p2] += sg[1] - sg[0]
        for ind in scores:
            self.fitness[ind] = scores[ind] * 1/len(self.bots)

    def generateRandomSolution(self):
        s = []
        #for i in range(self.pop_size):
        for i in range(length):
            s += random.uniform(0,1)
        return s

    def generateInitPopulation(self):
        for i in range(len(self.bots)):
            self.pop.append(self.generateRandomSolution())
        self.generatePopulationFitness()


    def pickFitParent(self):
        self.fitness += abs(min(self.fitness)) + 1
        total_fitness = sum(self.fitness)
        r = random.randrange(total_fitness)
        ind = -1
        while r > 0:
            ind += 1
            r -= self.fitness[ind]
        return self.pop[ind]

    def pickBestN(self, n):
        bestGenomes = []
        for i in range(n):
            max_value = max(self.fitness)
            max_index = self.fitness.index(max_value)
            bestGenomes.append(self.pop.pop(max_index)) #remove best from population
            self.pop_fitnesses.pop(max_index)   #remove best from fitnesses
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
        max_ind = self.pop_fitnesses.index(max(self.pop_fitnesses))
        return self.pop[max_ind]

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
        self.pop = new_pop

    def evolve(self, number_epochs, mutation = .01, min_mutation = .001, shrink = .95):
        self.generateInitPopulation()
        self.generatePopulationFitness()
        print("self.fitness: ", self.fitness)
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