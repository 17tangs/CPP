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
        self.size = len(self.pop)
        self.best = self.pop[0].dis
        self.worst = self.pop[self.size-1].dis
        self.average = self.avg()
        self.rang = self.worst-self.best
        
    def stat(self):
        return "best: " + str(self.pop[0].dis) + "  worst: " + str(self.pop[len(self.pop)-1].dis) + "  average: " + str(self.avg()) + "  range: " + str(self.pop[len(self.pop)-1].dis - self.pop[0].dis) + "  size: " + str(len(self.pop))
    
    def add_random(self, n):
        for i in range(n):
            l = []
            co = copy.deepcopy(Population.CO)
            for k in range(48):
                l.append(co[RC[i][k]])
                co.remove(co[RC[i][k]])
            s = Solution(l)
            self.pop.append(s)    
        self.pop.sort(key = lambda l : l.dis)        
        self.rm_dup()
        self.update()
        
    def exp(self):
        l = []
        #print int(len(self.pop)*0.8+1)
        for i in range(1,781,1):
            l.append((0.0374879/(i**0.5))-0.001333185)
        return l

    def half_cut(self):
        prob = self.exp()
        prob[0] -= 0.00000128292
        parent1 = np.random.choice(self.pop[:780], 400, True, prob)
        parent2 = np.random.choice(self.pop[:780], 400, True, prob)
        children = []
        for i in range(len(parent1)):
            child = parent1[i].half(parent2[i])
            if randint(1,10)>7:
                child.mutate_reverse()
            children.append(child)
        self.pop[780:] = children
        self.pop.sort(key = lambda l:l.dis)
        self.rm_dup()
        self.update()
        
            
    def avg(self):
        n = 0
        for s in self.pop:
            n += s.dis
        return n/(len(self.pop))
    
    def weeve1(self):
        children = []
        i = 0
        k = i + len(self.pop)/2
        while(k<len(self.pop)):
            children.append(self.pop[i].weeve(self.pop[k]))
            i += 1 
            k = i + len(self.pop)/2
        self.pop = self.pop[:len(self.pop)/2] + children
        self.pop.sort(key = lambda l:l.dis)
        self.rm_dup()        

    
        
    def greedy(self):
        for i in range(len(C)):
            l = Solution([Population.CO[i]])
            l.seed_greedy(0)
            self.pop.append(l)
        self.pop.sort(key = lambda l : l.dis)        
        self.rm_dup()
        
    def rm_dup(self):
        k = []
        for i in range(len(self.pop)-1):
            if self.pop[i].dis == self.pop[i+1].dis:
                k.append(self.pop[i])
        for i in range(len(k)):
            self.pop.remove(k[i])
                
    
    #normalize solution to start on specific city b
    def normalize(self, l, b):
        l = l[l.index(b):] + l[:l.index(b)]
        return l    
    
    
    
    
    
    
"""
dumpster, don't delete
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
            