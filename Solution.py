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
        
    def weeaave(self,s,n):
        p1 = copy.deepcopy(self.sol)
        p2 = copy.deepcopy(s.sol)
        ci = []        
        self.weave(p1,p2,0,ci,n)
        child = Solution(ci)
        print child
        return child
    
    def weave(self,p1,p2,i,c,n):
        if len(c) + n >= len(p1):
            return
        k = 0
        j = i
        while j < i+n+k:
            if p1[j%len(p1)].b == True:
                c.append(p1[j%len(p1)])
                p1[j%len(p1)].b = False                
            else:
                k += 1
            j +=1
        i = (p2.index(c[len(c)-1])+1)%len(p1)
        for v in c:
            p2[p2.index(v)].b = False
        k = 0
        j = i
        while j < i+n+k:
            if p2[j%len(p2)].b == True:
                c.append(p2[j%len(p2)])
                p2[j%len(p2)].b = False                
            else:
                k += 1    
            j+=1
        i = (p1.index(c[len(c)-1])+1)%len(p1)
        for v in c:
            p1[p1.index(v)].b = False
        self.weave(p1,p2,i,c,n)
        
        

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
        
    #a mutation that takes a random section of the solution and moves it to another section of the solution.
    def mutate_shift(self):
        l = randint(3, 6)
        s = randint(0, len(self.sol)-l-1)
        c = randint(0, len(self.sol)-l-1)
        cities = self.sol[c:c+l]
        del self.sol[c:c+l]
        for i in range(0, l):
            self.sol.insert(s+i, cities[i])
    
    

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



s1 = [3,14,15,9,2,6,5,8,7,13,12,18,16,1,10,19,11,20,4,17]
s2 = [2,13,6,18,3,16,4,11,19,1,14,9,17,20,15,5,8,7,10,12]
x = Solution([])
c = []

