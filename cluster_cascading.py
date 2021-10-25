#Studying the effect of Cascading on a Cluster with Density 

import networkx as nx
import matplotlib.pyplot as plt
import random

def set_all_B(G):
    for each in G.nodes():
        G.nodes[each]['action'] = 'B'

def set_A(G,list):
    for each in list:
        G.nodes[each]['action'] = 'A'

def get_colors(G):
    list = []
    for each in G.nodes():
        if(G.nodes[each]['action']=='B'):
            list.append('red')
        else:
            list.append('green')
    return list


def find_neigh(each,G,C):
    num = 0
    for each1 in G.neighbors(each):
        if( G.nodes[each1]['action']==C):
            num = num + 1
    return num


def recalculate_options(G):
    dict = {}
    a = 3 #Payoff of nodes with 'A'
    b = 2 #Payoff of nodes with 'B'

    for each in G.nodes():
        num_A = find_neigh(each, G, 'A')
        num_B = find_neigh(each, G, 'B')
        payoff_A = a * num_A
        payoff_B = b * num_B
        if(payoff_A >= payoff_B):
            dict[each] = 'A'
        else:
            dict[each] = 'B'
    return dict

def reset_node_attributes(G,action_dict):
    for each in action_dict:
        G.nodes[each]['action'] = action_dict[each]

def terminate_1(c,G):
    f = 1
    for each in G.nodes():
        if G.nodes[each]['action']!=c:
            f = 0
            break
    return f

def terminate(G,count):
    flag1 = terminate_1('A', G)
    flag2 = terminate_1('B', G)
    if flag1 == 1 or flag2 == 1 or count>=100:
        return 1
    else:
        return 0





G = nx.Graph()
G.add_edges_from([(0,1),(0,6),(1,2),(1,8),(1,12),(2,9),(2,12),(3,4),(3,9),(3,12),(4,5),(4,12),(5,6),(5,10),(6,8),(7,8),(7,9),(7,10),(7,11),(8,9),(8,10),(8,11),(9,10),(9,11),(10,11)])
#nx.draw(G,node_size=800,with_labels=True)
#plt.show()

list = [[0,1,2,3],[0,2,3,4],[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,12],[2,3,4,12],[0,1,2,3,4,5],[0,1,2,3,4,5,6,12]]

for list1 in list:
    print(list1)
    set_all_B((G))
    set_A(G,list1)
    colors = get_colors(G)
    #nx.draw(G,node_color=colors,node_size=800,with_labels=True)
    #plt.show()
    flag = 0
    count = 0
    while(1):
        flag = terminate(G,count)
        if flag == 1:
            break
        count = count + 1
        action_dict = recalculate_options(G)
        reset_node_attributes(G, action_dict)
        colors = get_colors(G)
        #nx.draw(G,node_color=colors,node_size=800,with_labels=True)
        #plt.show()
    #print("Number of Iterations = ",count)
    c = terminate_1('A', G)
    if c == 1:
        print("Cascade is Completed")
    else:
        print("Cascade Incomplete")
    nx.draw(G,node_color=colors,node_size=800,with_labels=True)
    plt.show()