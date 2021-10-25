#Implementation of the Rich Getting Richer Phenomenon

import networkx as nx 
import random
import matplotlib.pyplot as plt


def display_graph(G,i,ne):
    pos = nx.circular_layout(G)
    if i=='' and ne == '':
        new_node = []
        rest_nodes = G.nodes()
        new_edges = []
        rest_edges = G.edges()
    else:
        new_node = [i]
        rest_nodes = list(set(G.nodes()) - set(new_node))
        new_edges = ne
        rest_edges = list(set(G.edges())-set(new_edges)-set([(b,a) for (a,b) in new_edges]))
    
    nx.draw_networkx_nodes(G,pos,nodelist=new_node,node_color='g')
    nx.draw_networkx_nodes(G,pos,nodelist=rest_nodes,node_color='r')
    nx.draw_networkx_edges(G,pos,edgelist=new_edges,edge_color='g',style = 'dashdot')
    nx.draw_networkx_edges(G,pos,edgelist=rest_edges,edge_color='r')
    plt.show()

def add_nodes(G,n,m0):
    m = m0-1

    for i in range(m0+1,n+1):
        G.add_node(i)
        degrees = dict(nx.degree(G))
        node_probabilities = {}

        for each in G.nodes():
            node_probabilities[each] = (float)(degrees[each]/sum(degrees.values()))

        node_probabilities_cumulative = []
        prev = 0
        for n,p in node_probabilities.items():
            temp = [n,prev+p]
            node_probabilities_cumulative.append(temp)
            prev = prev+p

        new_edges = []
        num_edges_added = 0
        target_nodes = []
        while(num_edges_added<m):
            prev_cumulative = 0
            r = random.random()
            k = 0
            while(not(r>prev_cumulative and r <= node_probabilities_cumulative[k][1])):
                prev_cumulative = node_probabilities_cumulative[k][1]
                k+=1

            target_node = node_probabilities_cumulative[k][0]
            if target_node in target_nodes:
                continue
            else:
                target_nodes.append(target_node)
            G.add_edge(i,target_node)
            num_edges_added+=1
            new_edges.append((i,target_node))

        #display_graph(G, i, new_edges)

    return G

def plot_degree_distribution(G):

    all_degrees=dict(nx.degree(G)).values()
    unique_degrees = list(set(all_degrees))
    unique_degrees.sort()
    count_of_degrees=[]

    for i in unique_degrees:
        c = list(all_degrees).count(i)
        count_of_degrees.append(c)

    plt.plot(unique_degrees,count_of_degrees,'ro-')
    plt.xlabel('Degrees')
    plt.ylabel('Number of Nodes')
    plt.title('Degree Distribution')
    plt.show()




def main():
    n = 500
    m0 = random.randint(2,n/5)
    G = nx.path_graph(m0)
    

    #display_graph(G, '', '')
    G = add_nodes(G,n,m0)
    plot_degree_distribution(G)


main()
