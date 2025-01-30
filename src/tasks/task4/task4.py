import uuid
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def insert_into_heap(root, key):
    def insert_implementation(root,node, key):
        queue = [node]
        while queue:
            curr = queue.pop(0)

            if not curr.left:
                curr.left = Node(key)
                heapify_up(root,curr.left)
                break
            else:
                queue.append(curr.left)

            if not curr.right:
                curr.right = Node(key)
                heapify_up(root,curr.right)
                break
            else:
                queue.append(curr.right)
    if not root:
        root = Node(key)
    else:
        insert_implementation(root,root, key)
    
def heapify_up(root, node):
        while node != root:
            parent = get_parent(root,node)
            if parent and node.val > parent.val:
                parent.val, node.val = node.val, parent.val
                node = parent
            else:
                break
def get_parent(root, node):
        # Шукаємо батьківський вузол для даного
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr.left == node or curr.right == node:
                return curr
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return None

root = Node(10)
insert_into_heap(root, 5)
draw_tree(root)
insert_into_heap(root, 12)
draw_tree(root)
insert_into_heap(root, 8)
draw_tree(root)
insert_into_heap(root, 7)
draw_tree(root)
insert_into_heap(root, 14)
draw_tree(root)
insert_into_heap(root, 45)
draw_tree(root)
insert_into_heap(root, 67)
draw_tree(root)
insert_into_heap(root, 55)
draw_tree(root)
insert_into_heap(root, 34)
draw_tree(root)

# Відображення дерева
draw_tree(root)
