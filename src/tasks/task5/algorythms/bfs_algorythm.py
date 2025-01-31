from collections import deque
from classes import Binary_tree
from .color_darkening_algorythm import darkening_color

def bfs_algorythm(graph: Binary_tree):
    matrix=graph.ancestorMatrix()
    start=graph.root.val
    visited = set()
    visit_order=[]
    queue = deque([f'{start}'])

    while queue:
        vertex = f'{queue.popleft()}'
        if vertex not in visited:
            visit_order.append(vertex)
            visited.add(vertex)
            queue.extend(set(matrix[vertex]) - visited)
    amount=1
    for i in visit_order:
        color=graph.get_node(int(i)).color
        darker=darkening_color(color,amount)
        graph.get_node(int(i)).set_color(darker)
        amount+=1
        
    return visit_order  




