from .node import Node

import networkx as nx
import matplotlib.pyplot as plt


class Binary_tree():
    def __init__(self, root) -> None:
        self.root = Node(root)

    def insert_into_heap(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self.__insert_implementation(self.root, key)

    def __nodeCount(self, root):
        if root is None:
            return 0
        return self.__nodeCount(root.left) + self.__nodeCount(root.right) + 1

    def __ancestorMatrixRecur(self, root, mat, anc):
        if root is None:
            return
        curr = root.val
        mat[f'{curr}']=[]

        if root.left is not None:
            mat[f'{curr}'].append(f'{root.left.val}')
        if root.right is not None:
            mat[f'{curr}'].append(f'{root.right.val}')
        if self.__get_parent(root) is not None:
            mat[f'{curr}'].append(f'{self.__get_parent(root).val}')



        anc.append(curr)

        self.__ancestorMatrixRecur(root.left, mat, anc)
        self.__ancestorMatrixRecur(root.right, mat, anc)

        anc.pop()
    def get_node(self,key):
        if self.root == None:
            return
        node= self.__get_node_impl(self.root, key)
        return node
    def __get_node_impl(self,root,key):
        if root is None:
            return
        if root.val==key:
            return root
        res1=self.__get_node_impl(root.left,key)
        if res1:
            return res1
        res2=self.__get_node_impl(root.right,key)
        if res2:
            return res2
        
    def reset_colors(self):
        base_color='#52d4ff'
        self.__reset_colors_impl(self.root, base_color)

    
    def __reset_colors_impl(self,root,color):
        if root is None:
            return
        self.__reset_colors_impl(root.left,color)
        root.set_color(color)
        self.__reset_colors_impl(root.right,color)


    def ancestorMatrix(self):
        if self.root is None:
            return []

        n = self.__nodeCount(self.root)

        mat={}

        anc = []

        self.__ancestorMatrixRecur(self.root, mat, anc)

        return mat

    def __insert_implementation(self, node, key):
        queue = [node]
        while queue:
            curr = queue.pop(0)

            if not curr.left:
                curr.left = Node(key)
                self.__heapify_up(curr.left)
                break
            else:
                queue.append(curr.left)

            if not curr.right:
                curr.right = Node(key)
                self.__heapify_up(curr.right)
                break
            else:
                queue.append(curr.right)

    def __heapify_up(self, node):
        while node != self.root:
            parent = self.__get_parent(node)
            if parent and node.val > parent.val:
                parent.val, node.val = node.val, parent.val
                node = parent
            else:
                break

    def __get_parent(self, node):
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if curr.left == node or curr.right == node:
                return curr
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return None

    def __add_edges(self, graph, node, pos, x=0, y=0, layer=1):
        if node is not None:
            graph.add_node(node.id, color=node.color, label=node.val)
            if node.left:
                graph.add_edge(node.id, node.left.id)
                l = x - 1 / 2 ** layer
                pos[node.left.id] = (l, y - 1)
                l = self.__add_edges(graph, node.left, pos,
                                     x=l, y=y - 1, layer=layer + 1)
            if node.right:
                graph.add_edge(node.id, node.right.id)
                r = x + 1 / 2 ** layer
                pos[node.right.id] = (r, y - 1)
                r = self.__add_edges(graph, node.right, pos, x=r,
                                     y=y - 1, layer=layer + 1)
        return graph

    def draw_tree(self):
        tree = nx.DiGraph()
        pos = {self.root.id: (0, 0)}
        tree = self.__add_edges(tree, self.root, pos)
        colors = [node[1]['color'] for node in tree.nodes(data=True)]
        labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
        plt.figure(figsize=(8, 5))
        nx.draw(tree, pos=pos, labels=labels, arrows=False,
                node_size=2500, node_color=colors)
        plt.show()
