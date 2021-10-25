#Page Ranking using Equal Points Distribution Method

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


def initialize_points(G):
    points = [100 for i in range(G.number_of_nodes())]
    return points


def distribute_points(G,points):
    prev_points = points
    new_points = [0 for i in range(G.number_of_nodes())]

    for i in G.nodes():
        out = G.out_edges(i)
        if len(out)==0:
            new_points[i]+=prev_points[i]
        else:
            share = prev_points[i]/len(out)
            for each in out:
                new_points[each[1]] += share

    return G,new_points

def handle_points_sink(G,points):
    for i in range(len(points)):
        points[i] = (float)(points[i])*0.8

    n = G.number_of_nodes()
    extra = ((float)(n)*100*0.2)/n
    for i in range(len(points)):
        points[i]+=extra
    return points



def keep_distributing_points(G,points):
    prev_points = points
    print("Enter # to stop")
    while(1):
        G,new_points = distribute_points(G,prev_points)
        print(new_points)

        new_points = handle_points_sink(G,new_points)

        char = input()
        if char == '#':
            break
        prev_points = new_points
    
    return G,new_points


def get_nodes_sorted_by_points(points):
    points_array = np.array(points)
    nodes_sorted_by_points = np.argsort(points_array)
    return nodes_sorted_by_points



def main():
    G=nx.DiGraph()
    G.add_nodes_from([i for i in range(10)])
    add_edges(G,0.3)

    points = initialize_points(G)
    print("Initial Points:")
    print(points)

    G,points = keep_distributing_points(G,points)

    nodes_sorted_by_points = get_nodes_sorted_by_points(points)
    print("Nodes sorted by points:")
    print(nodes_sorted_by_points)

    #Comparing with inbuilt function
    #pr = nx.pagerank(G)
    #pr_sorted = sorted(pr.items(),key = lambda x:x[1],reverse=True)

    #for i in pr_sorted:
        #print(i)


main()