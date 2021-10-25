import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node("Hello")
#print(G.nodes())

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(4,6)
G.add_edge(5,4)
G.add_edge(2,3)
G.add_edge(2,6)

#print(G.edges())

nx.draw(G,with_labels=1)
plt.show()