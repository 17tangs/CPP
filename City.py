from R import *

class City:
    def __init__(self, na = ""):
        #takes in a string and sets it equal to self.name
        self.name = na
        #using the data from R.py, references the coordinates of the city
        self.lat = float(CCOR[C.index(na)][1])
        self.lon = float(CCOR[C.index(na)][2])
        #finds the list that ranks the other cities from closest to furthest
        self.s = CS[C.index(na)]
        
    #function that finds the distance between two cities    
    def getDist(self,c): 
        return CDIS[C.index(self.name)][C.index(c)]    
    
    def __repr__(self):
        return self.__str__()
    
    #allows objects to be printed as strings
    def __str__(self):
        return self.name
    
    #makes objects comparable to one another
    def __eq__(self, other):
        return self.name == other.name
        
