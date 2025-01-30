import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G:nx.Graph):
    pos = nx.kamada_kawai_layout(G)
    plt.figure(figsize=(6, 6))

    nx.draw(G, pos, with_labels=True, node_size=120,node_color="skyblue", font_size=6, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()