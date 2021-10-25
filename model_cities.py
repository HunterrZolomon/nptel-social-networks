import networkx as nx
import matplotlib.pyplot as plt
import random

G=nx.Graph() #Undirected Graph
city_set = ['Delhi','Bangalore','Hyderabad','Ahmedabad','Chennai','Kolkata','Surat','Pune','Jaipur']

for each in city_set:
    G.add_node(each)

costs=[]
value=100
while(value<=2000):
    costs.append(value)
    value = value + 100

#print(costs)

while(G.number_of_edges() < 16):
    c1 = random.choice(G.nodes())
    c2 = random.choice(G.nodes())
    if c1!=c2 and G.has_edge(c1,c2)==0 :
        W = random.choice(costs)
        G.add_edge(c1,c2,weight=W)


nx.draw(G,with_labels=1)
plt.show()