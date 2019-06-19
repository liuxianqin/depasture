#coding=utf-8

import networkx as nx
import matplotlib.pyplot as plt

def drawGraph(adj_matrix,v_nums,e_nums):
	graph=nx.Graph(adj_matrix)
	
	point=[]
	for i in range(v_nums):
		point.append(i)
	position = nx.circular_layout(graph)
	nx.draw_networkx_nodes(graph,position, nodelist=point, node_color="r")
	nx.draw_networkx_edges(graph,position)
	nx.draw_networkx_labels(graph,position)    
	 
	plt.show()
