from .color_darkening_algorythm import darkening_color

def dfs_algorythm(graph):
    matrix=graph.ancestorMatrix()
    start_vertex=graph.root.val
    visited = set()
    visit_order=[]


    stack = [start_vertex]  
    while stack:
        vertex = f'{stack.pop()}'
        if vertex not in visited:
            visit_order.append(vertex)
            visited.add(vertex)
            stack.extend(reversed(matrix[vertex]))

    amount=1
    for i in visit_order:
        color=graph.get_node(int(i)).color
        darker=darkening_color(color,amount)
        graph.get_node(int(i)).set_color(darker)
        amount+=1
        
    return visit_order  


