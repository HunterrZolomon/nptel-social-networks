#Implementation of Fatman Evolutionary Model

import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import time


def create_graph():
    G = nx.Graph()
    #G.add_nodes_from(range(1,101))
    for i in range(1,101):
        G.add_node(i)
    
    return G



def assign_bmi(G):
    for each in G.nodes():
        G.nodes[each]['name'] = random.randint(15,40)
        G.nodes[each]['type'] = 'person'

def get_labels(G):
    dict1 = {}
    for each in G.nodes():
        dict1[each] = G.nodes[each]['name']
    return dict1

def get_size(G):
    arr1 = []
    for each in G.nodes():
        if G.nodes[each]['type'] == 'person':
            arr1.append(G.nodes[each]['name']*20)
        else:
            arr1.append(1000)
    return arr1

def get_colors(G):
    c = []
    for each in G.nodes():
        if G.nodes[each]['type'] == 'person':
            if G.nodes[each]['name'] == 15:
                c.append('green')
            elif G.nodes[each]['name'] == 40:
                c.append('yellow')
            else:  
                c.append('blue')
        else:
            c.append('red')

    return c


def add_foci_nodes(G):
    n = G.number_of_nodes()
    i = n + 1
    foci_nodes = ['gym','eatout','movie_club','karate_club','yoga_club']
    for j in range(0,5):
        G.add_node(i)
        G.nodes[i]['name'] = foci_nodes[j]
        G.nodes[i]['type'] = 'foci'
        i = i + 1

def get_foci_nodes():
    f = []
    for each in G.nodes():
        if G.nodes[each]['type'] == 'foci':
            f.append(each)
    return f

def get_person_nodes():
    p = []
    for each in G.nodes():
        if G.nodes[each]['type'] == 'person':
            p.append(each)
    return p

def add_foci_edges(G):
    foci_nodes = get_foci_nodes()
    person_nodes = get_person_nodes()

    for each in person_nodes:
        r = random.choice(foci_nodes)
        G.add_edge(each,r)


def homophily(G):
    pnodes = get_person_nodes()
    for u in pnodes:
        for v in pnodes:
            if u!=v:
                diff = abs(G.nodes[u]['name'] - G.nodes[v]['name'])
                p = float(1)/(diff + 1000)
                r = random.uniform(0,1)
                if r<p:
                    G.add_edge(u,v)

#finding number of common neighbours
def cmn(u,v,G):
    nu = set(G.neighbors(u))
    nv = set(G.neighbors(v))
    return len(nu & nv)


def closure(G):
    arr1 = []
    for u in G.nodes():
        for v in G.nodes():
            if u!=v and (G.nodes[u]['type'] == 'person' or G.nodes[v]['type'] == 'person'):
                k = cmn(u,v,G)
                p = 1-math.pow((1-0.1),k)
                tmp = []
                tmp.append(u)
                tmp.append(v)
                tmp.append(p)
                arr1.append(tmp)

    for each in arr1:
        u = each[0]
        v = each[1]
        p = each[2]
        r = random.uniform(0,1)
        if r<p:
            G.add_edge(u,v)

#Change in BMI because of Social Influence
def change_bmi(G):
    fnodes = get_foci_nodes()
    for each in fnodes:
        if G.nodes[each]['name'] == 'eatout':
            for each1 in G.neighbors(each):
                if G.nodes[each1]['name']!=40:
                    G.nodes[each1]['name'] += 1

        if G.nodes[each]['name'] == 'gym':
            for each1 in G.neighbors(each):
                if G.nodes[each1]['name']!=15:
                    G.nodes[each1]['name'] -= 1


def visualize(G):
    #time.sleep(1)
    labeldict = get_labels(G)
    nodesize = get_size(G)
    colorArr = get_colors(G)
    nx.draw(G,labels = labeldict,node_size = nodesize,node_color = colorArr)
    plt.show()

G = create_graph()
assign_bmi(G)
add_foci_nodes(G)
add_foci_edges(G)
#time.sleep(10)
visualize(G)
for t in range(1,10):
    homophily(G)
    closure(G)
    change_bmi(G)
    visualize(G)
