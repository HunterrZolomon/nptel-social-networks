#Implementation of +ve, -ve edges and Making a graph stable if it is unstable

import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools


def get_signs_of_tris(list,G):
    all_signs = []
    for i in range(len(list)):
        temp = []
        temp.append(G[list[i][0]][list[i][1]]['sign'])
        temp.append(G[list[i][1]][list[i][2]]['sign'])
        temp.append(G[list[i][2]][list[i][0]]['sign'])
        all_signs.append(temp)
    return all_signs


def count_unstable(all_signs):
    stable = 0
    unstable = 0
    for i in range(len(all_signs)):
        if all_signs[i].count('+') == 3 or all_signs[i].count('+') == 1:
            stable += 1
        elif all_signs[i].count('+') == 2 or all_signs[i].count('+') == 0:
            unstable += 1

    #print('Number of Total Triangles = ',stable+unstable)
    #print('Number of Stable Triangles = ',stable)
    #print('Number of Unstable Triangles = ',unstable)
    #print('---------------------------------------')
    return unstable


def stabilize(G,tri_list,all_signs):
    found_unstable = False
    while(found_unstable == False):
        index = random.randint(0,len(tri_list)-1)
        if all_signs[index].count('+') == 2 or all_signs[index].count('+') == 0:
            found_unstable = True
        else:
            continue
            
    r = random.randint(1,3)
    if all_signs[index].count('+') == 2:
        if r == 1:
            if G[tri_list[index][0]][tri_list[index][1]]['sign'] == '+':
                G[tri_list[index][0]][tri_list[index][1]]['sign'] = '-'
            elif G[tri_list[index][0]][tri_list[index][1]]['sign'] == '-':
                G[tri_list[index][0]][tri_list[index][1]]['sign'] = '+'
        elif r == 2:
            if G[tri_list[index][1]][tri_list[index][2]]['sign'] == '+':
                G[tri_list[index][1]][tri_list[index][2]]['sign'] = '-'
            elif G[tri_list[index][1]][tri_list[index][2]]['sign'] == '-':
                G[tri_list[index][1]][tri_list[index][2]]['sign'] = '+'
        elif r == 3:
            if G[tri_list[index][2]][tri_list[index][0]]['sign'] == '+':
                G[tri_list[index][2]][tri_list[index][0]]['sign'] = '-'
            elif G[tri_list[index][2]][tri_list[index][0]]['sign'] == '-':
                G[tri_list[index][2]][tri_list[index][0]]['sign'] = '+'

    elif all_signs[index].count('+') == 0:
        if r == 1:
            G[tri_list[index][0]][tri_list[index][1]]['sign'] = '+'
        elif r == 2:
            G[tri_list[index][1]][tri_list[index][2]]['sign'] = '+'
        elif r == 3:
            G[tri_list[index][2]][tri_list[index][0]]['sign'] = '+'

    return G


def see_coalitions(G):
    first_coalition = []
    second_coalition = []
    nodes = list(G.nodes())
    r = random.choice(nodes)

    first_coalition.append(r)

    processed_nodes = []
    to_be_processed = []
    to_be_processed.append(r)

    for each in to_be_processed:
        if each not in processed_nodes:
            neigh = [n for n in G.neighbors(each)]

            for i in range(len(neigh)):
                if G[each][neigh[i]]['sign'] == '+':
                    if neigh[i] not in first_coalition:
                        first_coalition.append(neigh[i])
                    if neigh[i] not in to_be_processed:
                        to_be_processed.append(neigh[i])

                elif G[each][neigh[i]]['sign'] == '-':
                    if neigh[i] not in second_coalition:
                        second_coalition.append(neigh[i])
                        processed_nodes.append(neigh[i])
            
            processed_nodes.append(each)

    return first_coalition,second_coalition





G = nx.Graph()
n = 7
G.add_nodes_from([i for i in range(1,n+1)])
mapping = {1:'Alexandra',2:'Anterim',3:'Bercy',4:'Bearland',5:'Eplex',6:'Gripa',7:'Ikly',8:'Jerma',9:'Lema',10:'Umesi',11:'Mexim',12:'Socialcity',13:'Tersi',14:'Xopia',15:'Tamara'}
G = nx.relabel_nodes(G,mapping)

signs = ['+','-']
for i in G.nodes():
    for j in G.nodes():
        if i!=j:
            G.add_edge(i,j,sign = random.choice(signs))



nodesList = G.nodes()
tri_list = [list(x) for x in itertools.combinations(nodesList,3)]
all_signs = get_signs_of_tris(tri_list,G)
unstable = count_unstable(all_signs)
unstable_track = [unstable]

while(unstable != 0):
    G = stabilize(G,tri_list,all_signs)
    all_signs = get_signs_of_tris(tri_list,G)
    unstable = count_unstable(all_signs)
    unstable_track.append(unstable)

#plt.bar([i for i in range(len(unstable_track))],unstable_track)
#plt.show()

first,second = see_coalitions(G)
#print(first)
#print(second)

edge_labels = nx.get_edge_attributes(G,'sign')
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G,pos,nodelist= first,node_color='red',node_size=500)
nx.draw_networkx_nodes(G,pos,nodelist= second,node_color='blue',node_size=500)
nx.draw_networkx_labels(G,pos,font_size=10)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_size=20,font_color='red')
plt.show()
