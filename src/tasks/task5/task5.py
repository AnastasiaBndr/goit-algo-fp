from classes import Binary_tree
from algorythms import dfs_algorythm,bfs_algorythm

root = Binary_tree(12)
root.insert_into_heap(10)
root.insert_into_heap(55)
root.insert_into_heap(123)
root.insert_into_heap(45)
root.insert_into_heap(78)
root.insert_into_heap(94)
root.insert_into_heap(67)
root.insert_into_heap(574)
root.insert_into_heap(44)
root.insert_into_heap(57)
root.insert_into_heap(32)
root.insert_into_heap(5)
print(bfs_algorythm(root))
root.draw_tree()
root.reset_colors()
print(dfs_algorythm(root))
root.draw_tree()



