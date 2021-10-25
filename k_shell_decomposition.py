#Implementation of Cores and K-Shell Decomposition

import networkx as nx 
import matplotlib.pyplot as plt 


def check_existence(H,d):
    f=0
    for each in H.nodes():
        if(H.degree(each)<=d):
            f=1
            break
    return f


def find(H,it):
    set1=[]
    for each in H.nodes():
        if(H.degree(each)<=it):
            set1.append(each)
    return set1



G = nx.Graph()
G.add_edges_from([(1,2),(3,11),(4,5),(5,6),(5,7),(5,8),(5,9),(5,10),(10,11),(10,13),(11,13),(12,14),(12,15),(13,14),(13,15),(13,16),(13,17),(14,15),(14,16),(15,16)])
H = G.copy()
it=1
tmp=[]
buckets=[]

while(1):
    flag=check_existence(H, it)
    if(flag==0):
        it=it+1
        buckets.append(tmp)
        tmp=[]
    if(flag==1):
        node_set=find(H,it)
        for each in node_set:
            H.remove_node(each)
            tmp.append(each)
    if(H.number_of_nodes()==0):
        buckets.append(tmp)
        break


print(buckets)

#nx.draw(G,with_labels=True)
#plt.show()