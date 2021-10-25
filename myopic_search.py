#Implementation of Decentralized/Myopic Search on a small world network and comparision to optimal search

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


def find_best_neighbour(G,c,v):
    dis = G.number_of_nodes()
    for each in G.neighbors(c):
        dis1 = len(nx.shortest_path(H,source=each,target=v))
        if(dis1<dis):
            dis = dis1
            choice = each
    return choice


def decentralized_search(G,u,v):
    path=[u]
    current=u
    while(1):
        w=find_best_neighbour(G, current, v)
        path.append(w)
        current=w
        if(current==v):
            break
    return path


def set_path_colors(G,p,p1):
    c=[]
    for each in G.nodes():
        if(each==p1[0]):
            c.append('red')
        if(each==p1[len(p1)-1]):
            c.append('red')
        if each in p and each in p1 and each!=p1[0] and each!=p1[len(p1)-1]:
            c.append('yellow')
        elif each in p and each not in p1 :
            c.append('blue')
        elif each in p1 and each not in p :
            c.append('green')
        elif each not in p and each not in p1:
            c.append('white')
    
    return c




G = nx.Graph()
G.add_nodes_from(range(0,50))
add_edges(G)

H=G.copy()

t=0

while(t<=10):
    add_weak_ties(G)
    t=t+1

start=0
destination=40

p = decentralized_search(G, start, destination)
p1 = nx.shortest_path(G,source=start,target=destination)
print(p)
print(p1)
colors = set_path_colors(G, p, p1)
#colors = set__optimal_path_colors(G, p1)
nx.draw(G,with_labels=True,node_color=colors)
plt.show()