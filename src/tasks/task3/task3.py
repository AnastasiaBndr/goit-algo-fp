from algorythm import dijkstra
import networkx as nx
import matplotlib
from graph import generate_graph, draw_graph
import random

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

def pretty_print_dict(d):
    pretty_dict = ''  
     
    for k, v in d.items():
        pretty_dict += f'{k}: {v}\n'
    return pretty_dict

points_amount=10


vertexes = random.sample(range(0, points_amount), points_amount)
ver_frequency= [random.randint(6,10) for _ in range(len(vertexes))]
edges = [[random.choices(vertexes, weights=ver_frequency)[0], random.choices(vertexes, weights=ver_frequency)[0]] for _ in range(len(vertexes)-1)]
weights=[random.randint(0, points_amount) for _ in range(0,len(edges))]

vertex=vertexes[0]

G = generate_graph(edges, vertexes,weights)

print(f"{bcolors.OKGREEN}Dijkstra for vertex {vertex}:\n{bcolors.ENDC} {pretty_print_dict(dijkstra(G, vertex))}")
draw_graph(G)
