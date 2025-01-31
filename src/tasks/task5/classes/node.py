import uuid


class Node:
    def __init__(self, key, color="#52d4ff"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())
    
    def set_color(self, hex_color):
        self.color=hex_color