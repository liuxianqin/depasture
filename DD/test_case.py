#coding=utf-8

from graph import Graph_Matrix
import networkx as nx
import matplotlib.pyplot as plt

def create_undirected_matrix(my_graph):
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    matrix = [[0, 1, 1, 1, 1, 1, 0, 0],  # a
              [0, 0, 1, 0, 1, 0, 0, 0],  # b
              [0, 0, 0, 1, 0, 0, 0, 0],  # c
              [0, 0, 0, 0, 1, 0, 0, 0],  # d
              [0, 0, 0, 0, 0, 1, 0, 0],  # e
              [0, 0, 1, 0, 0, 0, 1, 1],  # f
              [0, 0, 0, 0, 0, 1, 0, 1],  # g
              [0, 0, 0, 0, 0, 1, 1, 0]]  # h

    my_graph = Graph_Matrix(nodes, matrix)
    print(my_graph)
    return my_graph
    
 
def draw_undircted_graph(my_graph):
    G = nx.Graph()  # 建立一个空的无向图G
    for node in my_graph.vertices:
        G.add_node(str(node))
    for edge in my_graph.edges:
        G.add_edge(str(edge[0]), str(edge[1]))

    print("nodes:", G.nodes())  # 输出全部的节点： [1, 2, 3]
    print("edges:", G.edges())  # 输出全部的边：[(2, 3)]
    print("number of edges:", G.number_of_edges())  # 输出边的数量：1
    nx.draw(G, with_labels=True)
    plt.savefig("undirected_graph.png")
    plt.show()

if __name__=="__main__":
	my_graph=Graph_Matrix()
	create_undirected_matrix(my_graph)
	draw_undircted_graph(my_graph)
