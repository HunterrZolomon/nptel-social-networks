#Studying the effect of Communities on Cascading and Diffusion

import networkx as nx 
import random
import matplotlib.pyplot as plt

def create_first_community(G):
    for i in range(0,10):
        G.add_node(i)
    for i in range(0,10):
        for j in range(0,10):
            if i < j:
                r = random.uniform(0, 1)
                if r < 0.5 : 
                    G.add_edge(i,j)

def create_second_community(G):
    for i in range(11,20):
        G.add_node(i)
    for i in range(11,20):
        for j in range(11,20):
            if i < j:
                r = random.uniform(0, 1)
                if r < 0.5 : 
                    G.add_edge(i,j)

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
    a = 10 #Payoff of nodes with 'A'
    b = 5 #Payoff of nodes with 'B'

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
create_first_community(G)
create_second_community(G)
G.add_edge(5,15)



set_all_B((G))
list1 = [0,1]
set_A(G,list1)
colors = get_colors(G)

colors = get_colors(G)
nx.draw(G,node_color=colors,node_size=800,with_labels=True)
plt.show()

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
    nx.draw(G,node_color=colors,node_size=800,with_labels=True)
    plt.show()
#print("Number of Iterations = ",count)
c = terminate_1('A', G)
if c == 1:
    print("Cascade is Completed")
else:
    print("Cascade Incomplete")

