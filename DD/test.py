#coding=utf-8

import networkx as nx
import matplotlib.pyplot as plt


N=[[0, 3, 5, 1],[1, 5, 4, 3],[2, 1, 3, 5],[3, 5, 1, 4],[4, 5, 1, 3],[5, 3, 4, 1], [6, 3, 1, 4]]


G=nx.Graph()
point=[0,1,2,3,4,5,6]
G.add_nodes_from(point)
edglist=[]
for i in range(7):
    for j in range(1,4):
        edglist.append((N[i][0],N[i][j]))
G=nx.Graph(edglist)
position = nx.circular_layout(G)
nx.draw_networkx_nodes(G,position, nodelist=point, node_color="r")
nx.draw_networkx_edges(G,position)
nx.draw_networkx_labels(G,position)      
plt.show()
