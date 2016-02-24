import time
import numpy as np
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from Population import *
from R import *
from random import *
start_time = time.time()

#the best solution found on the internet at this time uses annealing
#after 400,000 iterations, the creator of that found the optimal distance to be 10,618 miles
#http://toddwschneider.com/posts/traveling-salesman-with-simulated-annealing-r-and-shiny/
class CPP:
    
    #number of iterations
    I = 50
    
    def main(self):
        #create a population class using Population.py
        p = Population()
        #generate the population based on the greedy algorithm
        p.greedy()
        #generate a certain number of random solutions
        p.add_random(957)
        #call and print the statistics of the iteration
        averages = []
        bests = []
        worsts = []
        for i in range(CPP.I):
            averages.append(p.average)
            bests.append(p.best)
            worsts.append(p.worst)
            p.half_cut()
        print p.stat()
        self.stat(averages,bests,worsts)
        self.draw(p.pop)
        
        
        
##DISPLAY
        
    #plots the cross-iteration trend of averages
    def stat(self, a, b, w):
        x = [i for i in range(CPP.I)]
        plt.plot(x, a)
        plt.plot(x, b)
        plt.plot(x, w)
        plt.axis([0,CPP.I,0,100000])
        plt.show()
        
    #draws a map of the US and displays the solutions graphically
    def draw(self, pop):
        fig=plt.figure()
        ax=fig.add_axes([0.1,0.1,0.8,0.8])
        m = Basemap(llcrnrlon=-125.,llcrnrlat=25.,urcrnrlon=-65.,urcrnrlat=52.,
                    rsphere=(6378137.00,6356752.3142),
                    resolution='l',projection='merc',
                    lat_0=40.,lon_0=-20.,lat_ts=20.)
        l = pop[0]          
        for i in range(len(l.sol)):
            lat1 = l.sol[i].lat
            lon1 = l.sol[i].lon
            m.drawgreatcircle(lon1,lat1,lon1,lat1, linewidth=4, color = 'r')
            if i == len(l.sol) - 1:
                lat2 = l.sol[0].lat
                lon2 = l.sol[0].lon
            else:
                lat2 = l.sol[i+1].lat
                lon2 = l.sol[i+1].lon
            m.drawgreatcircle(lon1,lat1,lon2,lat2, color = 'b')
        m.drawcoastlines()
        m.drawstates()
        m.drawcountries()
        m.fillcontinents()
        ax.set_title('GREEDY')
        plt.show()            
    
    
    
##RECYCLING BIN
    
        #Methods that read data.txt and generate the lists C, CCOR, CDIS and CS.
        #The data is exported to R.py where it can be referenced upon later.
        #Once they run, there's no need to run it again.    
"""
    def shortest(self, c, l):
        m = sys.maxint
        ind = 0
        for i in range(len(CDIS)):
            if C[i] not in l:
                if self.getDist(c, C[i]) != 0:
                    if self.getDist(c, C[i]) < m:
                        m = self.getDist(c, C[i])
                        ind = i
        return C[ind]

    def init(self):
        f = open("data.txt", "r")                                                
        for i in range(48):                                                      
            e = []
            for k in range(8):                                                   
                s = f.readline()
                if k % 2 == 0:
                    if(s[-2] == "\r"):
                        s = s[:-2]
                    else:
                        s = s[:-1]
                    #excluding empty lines and name of state
                    if(s[:4] != "Name"):  
                        #slicing string for only the name of capital and longtitude/latitude
                        e.append(s.split(":")[1][1:])
            #append each small list city list for 2D array
            CCOR.append(e)                                                       
        for y in range(len(CCOR)):
            dis = []
            for x in range(len(CCOR)):
                lat1 = radians(float(CCOR[x][1]))
                lon1 = radians(float(CCOR[x][2]))
                lat2 = radians(float(CCOR[y][1]))
                lon2 = radians(float(CCOR[y][2])) 
                dlon = lon2 - lon1 
                dlat = lat2 - lat1 
                a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2 
                n = 2 * atan2( sqrt(a), sqrt(1-a) ) 
                d = R * n
                dis.append(int(d))
            CDIS.append(dis)
        for z in range(len(CCOR)):
            C.append(CCOR[z][0])
        f1 = open("R.py", "w")
        f1.write("R = 6371\n")
        f1.write("C = " + str(C) + "\n" )
        f1.write("CCOR = " + str(CCOR) + "\n")
        f1.write("CDIS = " + str(CDIS) +  "\n")
        f1.close()    
    
    def seed_greedy(self, l,i):
        if i == len(C) - 1:
            return
        else:
            lis = [n.name for n in l]
            k = 0
            while l[i].s[k] in lis:
                k += 1
            l.append(CPP.CO[C.index(l[i].s[k])])
            self.seed_greedy(l,i + 1)
            
    def ss(self):
        CS = []
        for c in C:
            CS.append(self.s(c))
        f = open("R.py", "a")
        f.write("CS = " + str(CS))
        f.close()
        return
    
    def s(self, c):
        l = [c]
        for x in range(len(C)-1):
            m = sys.maxint
            ind = 0            
            for i in range(len(CDIS)):
                if C[i] not in l:
                    if self.getDist(c, C[i]) != 0:
                        if self.getDist(c, C[i]) < m:
                            m = self.getDist(c, C[i])
                            ind = i
            l.append(C[ind])

        return l    
    """



##CALLING MAIN FUNCTION
x = CPP()
x.main()
#printing the elapsed time to complete I iterations
print("--- %s seconds ---" % (time.time() - start_time))