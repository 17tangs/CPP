from Solution import *
from R import *
from random import *
import numpy as np

class Population:  

    CO = [City(C[i]) for i in range(len(C))]
    
    def __init__(self):
        self.pop = []
        self.best = 0
        self.worst = 0
        self.average = 0
        self.rang = 0
        self.size = 0
    
    def update(self):
        #the size of the population is the number of items in the pop list
        self.size = len(self.pop)
        #the best/last distance is the value of the very first/last solution
        self.best = self.pop[0].dis
        self.worst = self.pop[self.size-1].dis
        self.average = self.avg()
        self.rang = self.worst-self.best
        
   

##FUNCTIONS IN PROGRESS...
        
    def weave1(self):
        children = []
        i = 0
        k = i + len(self.pop)/2
        while(k<len(self.pop)):
            children.append(self.pop[i].weave(self.pop[k]))
            i += 1 
            k = i + len(self.pop)/2
        self.pop = self.pop[:len(self.pop)/2] + children
        self.pop.sort(key = lambda l:l.dis)
        self.rm_dup()        

    #function that determines how probable it is for a solution to breed based on its ranking
    #note: this is done by hand with magic numbers, and an actual function that can take in
    #varied population sizes will be written later
    def exp(self):
        l = []
        for i in range(1,781):
            l.append((0.0374879/(i**0.5))-0.001333185)
        return l

    #a breeding mechanism that "randomly" chooses two parents and
    #generates a child by combining the top and bottom halves
    def half_cut(self):
        prob = self.exp()
        prob[0] -= 0.00000128292
        parent1 = np.random.choice(self.pop[:780], 400, True, prob)
        parent2 = np.random.choice(self.pop[:780], 400, True, prob)
        children = []
        child = self.pop[0].weeaave(self.pop[0],4)
        print child
        #for i in range(len(parent1)):
            #child = parent1[i].weeaave(parent2[i],4)
            ##each child has a 3/10 chance of mutating
            #if randint(1,10)>7:
                #child.mutate_reverse()
            #if randint(1, 10)>7:
                #child.mutate_shift()
            #children.append(child)
        #adds the newly generated list of children to the population list and re-sorts
        #self.pop[780:] = children
        #self.pop.sort(key = lambda l:l.dis)
        #self.rm_dup()
        #self.update()
        


##SOLUTION GENERATION
        
    #a function that generates solutions based on the greedy algorithm,
    #which finds the closest city to the previous one
    def greedy(self):
        for i in range(len(C)):
            l = Solution([Population.CO[i]])
            l.seed_greedy(0)
            self.pop.append(l)
        self.pop.sort(key = lambda l : l.dis)        
        self.rm_dup()
        
    #generates n lists of random solutions
    def add_random(self, n):
        for i in range(n):
            l = []
            co = copy.deepcopy(Population.CO)
            #chooses 48 random cities and places them into list l
            for k in range(48):
                l.append(co[RC[i][k]])
                #removes the duplicates from the original list of city objects
                co.remove(co[RC[i][k]])
            #creates a solution based on the list l of cities called s
            s = Solution(l)
            #adds solution s to the list of populations
            self.pop.append(s)    
        #sorts the list of solutions according to their total distances
        self.pop.sort(key = lambda l : l.dis)        
        self.rm_dup()
        self.update()    
        
        
        
##POPULATION REGULATION        
        
    #normalizes solution to start on specific city b
    def normalize(self, l, b):
        l = l[l.index(b):] + l[:l.index(b)]
        return l          
    
    #checks for and deletes duplicates from the population
    def rm_dup(self):
        k = []
        #records the duplicate solutions in list k
        for i in range(len(self.pop)-1):
            if self.pop[i].dis == self.pop[i+1].dis:
                k.append(self.pop[i])
        #removes the recorded duplicates from the population list
        for i in range(len(k)):
            self.pop.remove(k[i])
        


##STATISTICS
            
    #finds the average distance of solutions in the population    
    def avg(self):
        n = 0
        for s in self.pop:
            n += s.dis
        return n/(len(self.pop))
    
    #function that displays all the statistics of the population
    def stat(self):
        return "best: " + str(self.pop[0].dis) + "  worst: " + str(self.pop[len(self.pop)-1].dis) + "  average: " + str(self.avg()) + "  range: " + str(self.pop[len(self.pop)-1].dis - self.pop[0].dis) + "  size: " + str(len(self.pop))    
    
    
    
##RECYCLING BIN
    
"""
    def half_cut1(self):
        children = []
        i = 0
        k = i + len(self.pop)/2
        while(k<len(self.pop)):
            children.append(self.pop[i].half(self.pop[k]))
            i += 1 
            k = i + len(self.pop)/2
        self.pop = self.pop[:len(self.pop)/2] + children
        self.pop.sort(key = lambda l:l.dis)
        self.rm_dup()
        
    def half_cut2(self):
        children = []
        for i in range(0,len(self.pop)-1, 2):
            children.append(self.pop[i].half(self.pop[i+1]))
        self.pop = self.pop[:(len(self.pop)*7/12)] + children
        self.pop.sort(key = lambda l:l.dis)
        self.rm_dup()
"""
            