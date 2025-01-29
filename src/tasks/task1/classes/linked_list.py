from .node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def pop_from_end(self):
        cur = self.head
        if cur and cur.next == None:
            temp = self.head
            self.head = None
            return temp
        while cur and cur.next != None:
            prev = cur
            cur = cur.next
        if cur.next is None:
            temp = cur
            prev.next = None
            cur = None
            return temp

    def reverse_list(self):
        if self.head and self.head.next == None:
            return self.head
        cur = self.head
        previous = None
        while cur:
            tmp = cur.next
            cur.next = previous
            previous = cur
            cur = tmp
        self.head = previous

    def length(self):
        length = 0
        curr = self.head
        while curr is not None:
            length += 1
            curr = curr.next
        return length

    def bubble_sort(self):
        curr = self.head
        len = self.length()
        itr = 0

        while itr < len:
            temp = self.head
            prevNode = self.head
            swapped = False

            while temp.next:
                temp_next = temp.next
                if temp.data > temp_next.data:
                    swapped = True

                    if temp == self.head:
                        temp.next = temp_next.next
                        temp_next.next = temp
                        prevNode = temp_next
                        self.head = prevNode
                    else:
                        temp.next = temp_next.next
                        temp_next.next = temp
                        prevNode.next = temp_next
                        prevNode = temp_next
                    continue
                prevNode = temp
                temp = temp.next
            if not swapped:
                break
            itr += 1
        return self.head
    
    def merge_list(self, list):
        list_len = list.length()

        for _ in range(list_len):
            node = list.pop_from_end()
            if node:
                self.insert_at_end(node.data)

        self.bubble_sort()
    
    def __str__(self) -> str:
        str=''
        curr = self.head
        while curr is not None:
            str+=f'{curr.data}'+' '
            curr = curr.next
        return str
