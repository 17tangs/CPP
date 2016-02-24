from R import * 
from City import *
import copy
from random import *

class Solution:
    
    CO = [City(C[i]) for i in range(len(C))]
    
    def __init__(self, arr=[]):
        self.sol = arr
        self.dis = self.total_distance(self.sol)
        
        
        
##FUNCTIONS IN PROGRESS...
        
    def weave(self,s):
        sol1 = copy.deepcopy(self.sol)
        sol2 = copy.deepcopy(s.sol)
        
    def weave1(self, s):
        child = []
        sol1 = copy.deepcopy(self.sol)
        sol2 = copy.deepcopy(s.sol)
        i = 0
        m = len(sol1)
        while len(child) <= m:
            while sol1[i] in child and i < len(sol1):
                i += 1
            if i == len(sol1) - 1:
                i = 0
                child.append(sol1[i])
            if sol2.index(sol1[i])+1 >= len(sol2):
                i = 0
                while sol2[i] in child:
                    i += 1
                if i == len(sol2)-1:
                    i = 0
                    child.append(sol2[i])
                if sol1.index(sol2[0]) + 1 >= len(sol1):
                    i = 0
                else:
                    i = sol1.index(sol2[0])+1
            else:
                while sol2[sol2.index(sol1[i])+1] in child:
                    i += 1
                if i == len(sol2)-1:
                    i = 0
                child.append(sol2[sol2.index(sol1[i])+1])
                if sol1.index(sol2[sol2.index(sol1[i])+1])+1 >= len(sol1):
                    i = 0
                else: 
                    i = sol1.index(sol2[sol2.index(sol1[i])+1])+1
        return Solution(child)
    
    
    
##SOLUTION GENERATION
    
    #uses the greedy algorith to generate a solution based on the closest cities
    def seed_greedy(self, i):
        #terminates the recursion when a sufficient number of solutions have been generated
        if i == len(C) - 1:
            self.dis = self.total_distance(self.sol)
            return
        else:
            lis = [n.name for n in self.sol]
            k = 0
            #finds the nest closest city that isn't already in the list and appends it to the solution
            while self.sol[i].s[k] in lis:
                k += 1
            self.sol.append(Solution.CO[C.index(self.sol[i].s[k])])
            self.seed_greedy(i + 1)
    
    
    
##BREEDING SOLUTIONS
    
    #this function pastes the bottom half of one solution to the top of another
    def half(self, s):
        k = []
        dom = copy.deepcopy(self.sol[:(len(self.sol)/2)])
        res = copy.deepcopy(s.sol)
        for c in res:
            if c in dom:
                k.append(c)
        for x in k:
            res.remove(x)
        return Solution(dom+res)
    
    
    
##RANDOM MUTATIONS
    
    #a mutation that chooses two random cities in a solution and switches their order
    def mutate_swap(self):
        k = randint(0,len(self.sol)-2)
        s = self.sol[k]
        self.sol[k] = self.sol[k+1]
        self.sol[k+1] = s
     
    #a mutation that chooses a random section of the solution and reverses its order
    def mutate_reverse(self):
        l = randint(2,25)
        k = randint(0,len(self.sol)-l-1)
        r = self.sol[k:k+l]
        r.reverse()
        self.sol[k:k+l] = r
        

    
##SOLUTION ATTRIBUTES
          
    #retrives the distance between two cities  
    def getDist(self,c1, c2): 
        return CDIS[C.index(c1)][C.index(c2)]     
    
    #find the total distance traveled for a particular solution l    
    def total_distance(self, l):
        if len(l) == 0:
            return 0
        d = 0
        for i in range(len(l)-1):
            d += self.getDist(l[i].name, l[i + 1].name)
        d += self.getDist(l[0].name, l[len(l) - 1].name)    
        return d    
    
    def __repr(self):
        return self.__str__()
    
    def __str__(self):
        return str(self.sol)