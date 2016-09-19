from __future__ import division
import random
import string
import io
import numpy as np
from ScrabbleBot import *
from ScrabbleGame import *
from ScrabblePlayer import *
from scrabble_globals import *
from ScrabbleBotter import *

length = 11 #length of genes

class GA:
    def __init__(self):
        self.bots = [] #list of genes? (doubles)
        self.fitnesses = []

    def generatePopulationFitness(self):
        pop_size = len(self.bots)
        print "GENERATING POPULATION FITNESS"
        scores = []
        mybots = []
        for i in range(pop_size): scores.append(0) #initializes list
        for p1 in range(pop_size-1):
            for p2 in range(p1+1, pop_size):
                sGame = ScrabbleGame(BOARD_SIZE)

                bot1 = ScrabbleBotter(sGame.drawTiles(RACK_MAX_SIZE), sGame, self.bots[p1])
                bot2 = ScrabbleBotter(sGame.drawTiles(RACK_MAX_SIZE), sGame, self.bots[p2])
                sg = sGame.playGame(bot1, bot2)

                scores[p1] = scores[p1] + (sg[0] - sg[1])
                scores[p2] += sg[1] - sg[0]

        for ind in range(len(scores)):
            self.fitnesses[ind] = scores[ind] * 1/pop_size

    def generateRandomSolution(self):
        s = []
        for i in range(length):
            s.append(random.uniform(0,1))
        return s

    def generateInitPopulation(self, pop_size):
        weights1 = [0.434552526983, 0.0695333713975, -0.244925612275, 0.151061392263, 0.504794041753, 0.468776347428, 0.644338989372, 0.54300419617, 1.18654167414, -0.246213177556, 0.769765798309]
        weights2 = [0.358398670334, -0.0258820809337, -0.0117747523405, -0.048199454868, 0.144839908045, 0.0998114509692, 0.68054231695, 0.64982813339, 0.921265680606, -0.102322611715, 0.732581560706]
        for i in range(pop_size-2):
            self.fitnesses.append(0)
            mybot = []
            for j in range(len(weights1)):
                mybot.append(random.uniform(weights1[j], weights2[j]))
                mybot[j]=np.random.normal(mybot[j], .2)
            self.bots.append(mybot)
        self.fitnesses.append(0)
        self.fitnesses.append(0)
        self.bots.append(weights1)
        self.bots.append(weights2)
        self.generatePopulationFitness()
        return


    def pickFitParent(self):
        theMin = abs(min(self.fitnesses))
        for i in range(len(self.fitnesses)):
            self.fitnesses[i] += theMin #pushing them all above 0
        total_fitnesses = round(sum(self.fitnesses))
        r = random.randrange(total_fitnesses)
        ind = -1
        while r > 0:
            ind += 1
            r -= self.fitnesses[ind]
        return self.bots[ind]

    def pickBestN(self, n):
        bestGenomes = []
        for i in range(n):
            #print self.fitnesses
            max_value = max(self.fitnesses)
            max_index = self.fitnesses.index(max_value)
            #print self.bots[max_index]
            bestGenomes.append(self.bots.pop(max_index)) #remove best from population
            self.bots.append(0)
            self.fitnesses.pop(max_index)   #remove best from fitnesses
            self.fitnesses.append(0)
        return bestGenomes

    def crossover(self, p1, p2):
        baby = []
        for i in range(len(p1)):
            #baby.append(random.choice((p1[i],p2[i])))
            baby.append(random.uniform(p1[i],p2[i]))
        return baby

    def mutate(self, child, mutation_rate):
        for weight in child:
            if random.random() < mutation_rate:
                weight = np.random.normal(weight, .1)
        return child

    def getBestSolution(self):
        max_ind = self.bots_fitnesses.index(max(self.bots_fitnesses))
        return self.bots[max_ind]

    def generateNewPopulation(self, mutation, survival=1):
        new_pop = []
        i = 0
        while i < len(self.bots)-survival:

            p1 = self.pickFitParent()
            p2 = self.pickFitParent()
            child = self.crossover(p1, p2)

            child = self.mutate(child, mutation)
            new_pop.append(child)
            i += 1
        bestN = self.pickBestN(survival)
        for item in bestN:
            new_pop.append(item)
        self.bots = new_pop
        return
    def logBest(self, num):
        try:
            fl=open("weights.txt", "a")
        except:
            print("could not open")
        max_index = self.fitnesses.index(max(self.fitnesses))
        bestBot = ''.join(str(e)+', ' for e in self.bots[max_index])
        print self.bots[max_index]
        #print bestBot
        fl.write(str(num))
        fl.write(" ")
        fl.write(bestBot)
        fl.write("\n")
        fl.close()
        return

    def evolve(self, pop_size, number_epochs, mutation = .3, min_mutation = .001, shrink = .95):

        self.generateInitPopulation(pop_size)
        self.logBest(-1)
        print("self.fitnesses: ", self.fitnesses)
        for i in range(number_epochs):
            print "GENERATION ", i
            self.generateNewPopulation(mutation)
            self.generatePopulationFitness()
            if mutation > min_mutation:
                mutation *= shrink
            self.logBest(i)
            print "done logging!"
        sys.exit(0)


if __name__=="__main__":
    ga = GA()
    ga.evolve(6, 10000)
