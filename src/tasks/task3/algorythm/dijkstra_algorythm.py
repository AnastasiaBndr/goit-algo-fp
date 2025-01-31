import networkx as nx
import heapq
import numbers

def dijkstra(graph:nx.Graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    heap=[(0,start)]
    
    while heap:
        current_distance, current_vertex=heapq.heappop(heap)
    
        if current_distance > distances[current_vertex]:
            continue
        print(graph[current_vertex].items())
        for neighbor, weight in graph[current_vertex].items():
            distance=current_distance+weight['weight']
            if distance<distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(heap,(distance, neighbor))


    return distances