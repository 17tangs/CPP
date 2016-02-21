from R import *

class City:
    def __init__(self, na = ""):
        self.name = na
        self.lat = float(CCOR[C.index(na)][1])
        self.lon = float(CCOR[C.index(na)][2])
        self.s = CS[C.index(na)]
        
    def getDist(self,c): 
        return CDIS[C.index(self.name)][C.index(c)]    
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other.name
        
