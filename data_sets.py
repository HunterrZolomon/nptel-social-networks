from itertools import count
import networkx as nx
import matplotlib.pyplot as plt

def plot_degree_distribution(G):
    all_degrees = nx.degree(G)
    unique_degrees = list(set(all_degrees))

    count_of_degrees = []
    for i in unique_degrees:
        x = all_degrees.count(i)
        count_of_degrees.append(x)

    plt.plot(unique_degrees,count_of_degrees)
    plt.show()



#G = nx.read_edgelist('Datasets/facebook_combined.txt')
G = nx.read_pajek("Datasets/football.net")
#G = nx.read_pajek('Datasets/karate.paj')
#G = nx.read_graphml('')
#G = nx.read_gexf('Datasets/EuroSiS_Generale_Pays.gexf')
#G = nx.read_gml('Datasets/karate.gml')



#print(nx.info(G))
#print(nx.is_directed(G))

#nx.draw(G)
#nx.draw_circular(G)
#plt.show()

plot_degree_distribution(G)