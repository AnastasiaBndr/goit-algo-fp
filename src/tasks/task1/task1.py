import random
from classes import LinkedList


llist = LinkedList()

for i in range(7):
    llist.insert_at_end(random.randint(1,100))

print(f'Linked list: {llist}')
llist.reverse_list()
print(f"Reversed list: {llist}")
llist.bubble_sort()
print(f"Bubble sorted list: {llist}")
print(f'------------------------------\n')

llist2=LinkedList()
for i in range(10):
    llist2.insert_at_end(random.randint(1,100))

print(f'New list: {llist2}')
llist.merge_list(llist2)
print(f"After merging: {llist}")

