#Community Detection using Girvan-Newman Algo based on Betweenness of an Edge

import networkx as nx


def edge_to_remove(G):
    dict1 = nx.edge_betweenness_centrality(G)
    list_of_tuples = dict1.items()
    sorted_list = list(reversed(sorted(list_of_tuples)))
    return sorted_list[0][0]



def girvan_newman(G):
    #c = nx.connected_component_subgraphs(G)
    c = (G.subgraph(i) for i in nx.connected_components(G))
    l = len(c)
    print("The number of connected components are ",l)

    
    while(l == 1):
        G.remove_edge(*edge_to_remove(G))
        c = list(G.subgraph(i) for i in nx.connected_components(G))
        l = len(c)
        print("The number of connected components are ",l)

    return c


G = nx.barbell_graph(5,0)
c = girvan_newman(G)

for i in c :
    print(i.nodes())
    print('............')

