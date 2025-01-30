import networkx as nx
import matplotlib.pyplot as plt

def generate_graph(edges,vertex,weights) -> nx.Graph:
    G = nx.Graph()
    for vert in vertex:
        G.add_node(vert)
    for edge, weight in zip(edges,weights) :
        G.add_weighted_edges_from([(edge[0], edge[1],weight)])
    return G
