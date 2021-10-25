#Implementation of Schelling Model of Spatial Segregation

from hashlib import new
import networkx as nx
import matplotlib.pyplot as plt
import random

N = 10
G = nx.grid_2d_graph(N,N)

#Adding Diagonal Edges
nodeList = list(G.nodes())
for u,v in nodeList:
    if(u+1 <= N-1) and (v+1 <= N-1):
        G.add_edge((u,v),(u+1,v+1))
    if(u+1 <= N-1) and (v-1 >= 0):
        G.add_edge((u,v),(u+1,v-1))
    

for n in G.nodes():
    G.nodes[n]['type'] = random.randint(0,2)

type1_node_list = [n for (n,d) in G.nodes(data = True) if d['type'] == 1]
type2_node_list = [n for (n,d) in G.nodes(data = True) if d['type'] == 2]
empty_cells = [n for (n,d) in G.nodes(data = True) if d['type'] == 0]

pos = dict((n,n) for n in G.nodes())
labels_of_graph = dict(((i,j),i*10+j) for i,j in G.nodes())

def display_graph(G):
    nodes_b = nx.draw_networkx_nodes(G,pos,node_color='blue',nodelist=type1_node_list)
    nodes_r = nx.draw_networkx_nodes(G,pos,node_color='red',nodelist=type2_node_list)
    nodes_w = nx.draw_networkx_nodes(G,pos,node_color='white',nodelist=empty_cells)

    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos,labels=labels_of_graph)
    plt.show()


def get_boundary_nodes(G):
    boundary_nodes_list = []
    for((u,v),d) in G.nodes(data = True):
        if u==0 or u==N-1 or v==0 or v==N-1:
            boundary_nodes_list.append((u,v))
    return boundary_nodes_list

def neighbours_of_internal_node(u,v):
    return[(u-1,v),(u+1,v),(u,v-1),(u,v+1),(u-1,v+1),(u+1,v-1),(u-1,v-1),(u+1,v+1)]

def neighbours_of_boundary_node(u,v):
    if u == 0 and v == 0:
        return[(0,1),(1,1),(1,0)]
    elif u == N-1 and v == N-1:
        return [(N-2,N-2),(N-1,N-2),(N-2,N-1)]
    elif u == N-1 and v == 0:
        return [(u-1,v),(u,v+1),(u-1,v+1)]
    elif u == 0 and v == N-1:
        return [(u+1,v),(u+1,v-1),(u,v-1)]
    elif u == 0:
        return [(u,v-1),(u,v+1),(u+1,v),(u+1,v-1),(u+1,v+1)]
    elif u == N-1:
        return [(u-1,v),(u,v-1),(u,v+1),(u-1,v+1),(u-1,v-1)]
    elif v == N-1:
        return [(u,v-1),(u-1,v),(u+1,v),(u-1,v-1),(u+1,v-1)]
    elif v == 0:
        return [(u-1,v),(u+1,v),(u,v+1),(u-1,v+1),(u+1,v+1)]

def get_unsatisfied_nodes_list(G,internal_nodes_list,boundary_nodes_list):
    unsatisfied_nodes_list = []
    t = 3 #threshold
    for u,v in G.nodes():
        type_of_this_node = G.nodes[(u,v)]['type']
        if type_of_this_node == 0:
            continue
        else:
            similar_nodes = 0
            if(u,v) in internal_nodes_list:
                neigh = neighbours_of_internal_node(u,v)
            elif(u,v) in boundary_nodes_list:
                neigh = neighbours_of_boundary_node(u,v)

            for each in neigh:
                if G.nodes[each]['type'] == type_of_this_node:
                    similar_nodes+=1

            if similar_nodes <= t:
                unsatisfied_nodes_list.append((u,v))
                
    return unsatisfied_nodes_list 
            
def satisfy_nodes(unsatisfied_nodes_list,empty_cells):
    if len(unsatisfied_nodes_list) != 0:
        node_to_shift = random.choice(unsatisfied_nodes_list)
        new_position = random.choice(empty_cells)

        G.nodes[new_position]['type'] = G.nodes[node_to_shift]['type']
        G.nodes[node_to_shift]['type'] = 0
        labels_of_graph[node_to_shift],labels_of_graph[new_position] = labels_of_graph[new_position],labels_of_graph[node_to_shift]

    else:
        pass



boundary_nodes_list = get_boundary_nodes(G)
internal_nodes_list = list(set(G.nodes())-set(boundary_nodes_list))

unsatisfied_nodes_list = get_unsatisfied_nodes_list(G,internal_nodes_list,boundary_nodes_list)
num_of_iterations = 0
while(len(unsatisfied_nodes_list)!=0):
    satisfy_nodes(unsatisfied_nodes_list,empty_cells)
    type1_node_list = [n for (n,d) in G.nodes(data = True) if d['type'] == 1]
    type2_node_list = [n for (n,d) in G.nodes(data = True) if d['type'] == 2]
    empty_cells = [n for (n,d) in G.nodes(data = True) if d['type'] == 0]
    #unsatisfied_nodes_list = get_unsatisfied_nodes_list(G,internal_nodes_list,boundary_nodes_list)
    num_of_iterations+=1

print('Number of Interations = ',num_of_iterations)
display_graph(G)