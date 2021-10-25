#Study on how the diameter of a network changes when a weak tie is added to a small world

import networkx as nx 
import matplotlib.pyplot as plt 
import random

def add_edges(G):
    list_nodes = list(G.nodes())
    n = G.number_of_nodes()
    for i in range(0,len(list_nodes)):
        G.add_edge(list_nodes[i],list_nodes[i-1])
        G.add_edge(list_nodes[i],list_nodes[i-2])
        target = i+1
        if target > n-1:
            target = target - n
        G.add_edge(list_nodes[i],target)
        target = i+2
        if target > n-1:
            target = target - n
        G.add_edge(list_nodes[i],target)


def add_weak_ties(G):
    list_nodes = list(G.nodes())
    v1 = random.choice(list_nodes)
    v2 = random.choice(list_nodes)
    while(v1==v2):
        v1 = random.choice(list_nodes)
        v2 = random.choice(list_nodes)
    G.add_edge(v1, v2)
    #print("Weak Tie Added")


G = nx.Graph()
G.add_nodes_from(range(0,50))
add_edges(G)

x=[0]
y=[nx.diameter(G)]
t=0

while(t<=100):
    add_weak_ties(G)
    t=t+1
    x.append(t)
    y.append(nx.diameter(G))

plt.xlabel('Number of Weak Ties Added')
plt.ylabel('Diameter')
plt.plot(x,y)

#nx.draw(G,with_labels=True)
plt.show()