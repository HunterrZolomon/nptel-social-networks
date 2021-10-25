import networkx as nx 
import numpy as np 
import matplotlib.pyplot as plt 
import random

def independent_cascade(G,s):
    just_infected=list(s)
    infected = list(s)
    while(1):
        print(just_infected)
        print(infected)
        print("--------------")
        if(len(just_infected)==0):
            return infected
        tmp=[]
        for each in just_infected:
            for each1 in G.neighbors(each):
                r = random.uniform(0, 1)
                if r<0.5 and each1 not in infected and each1 not in tmp:
                    tmp.append(each1)
        
        for each in tmp:
            infected.append(each)
        just_infected=list(tmp)




G = nx.Graph()
G.add_edges_from([(1,2),(3,11),(4,5),(5,6),(5,7),(5,8),(5,9),(5,10),(10,11),(10,13),(11,13),(12,14),(12,15),(13,14),(13,15),(13,16),(13,17),(14,15),(14,16),(15,16)])

seed = [3,8]
list1=independent_cascade(G,seed)
