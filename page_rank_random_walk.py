#Page ranking using Random Walk Method

import networkx as nx 
import random
import numpy as np

def add_edges(G,p):
    for i in G.nodes():
        for j in G.nodes():
            if i!=j:
                r = random.random()
                if r<=p:
                    G.add_edge(i,j)
                else:
                    continue
    
    return G


def random_walk(G):
    nodes = list(G.nodes)
    RW_points = [0 for i in range(G.number_of_nodes())]
    r = random.choice(nodes)
    RW_points[r] += 1
    out = list(G.out_edges(r))

    c = 0
    while(c!= 10000000):
        if(len(out)==0):
            focus = random.choice(nodes)
        else:
            r1 = random.choice(out)
            focus = r1[1]
        RW_points[focus]+=1
        out = G.out_edges(focus)
        c+=1
    
    return RW_points





def get_nodes_sorted_by_RW(points):
    points_array = np.array(points)
    nodes_sorted_by_RW = np.argsort(points_array)
    return nodes_sorted_by_RW



def main():
    G=nx.DiGraph()
    G.add_nodes_from([i for i in range(10)])
    add_edges(G,0.3)

    RW_points = random_walk(G)

    nodes_sorted_by_RW = get_nodes_sorted_by_RW(RW_points)
    print("Nodes sorted by Random Walk:")
    print(nodes_sorted_by_RW)
    
    #Comparing with inbuilt function
    pr = nx.pagerank(G)
    pr_sorted = sorted(pr.items(),key = lambda x:x[1],reverse=True)

    for i in pr_sorted:
        print(i)


main()