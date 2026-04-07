from typing import Optional

class CacheNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.key}, {self.val})"

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.head, self.tail = CacheNode(-1, -1), CacheNode(-1, -1)
        self.head.right, self.tail.left = self.tail, self.head

    def insert_node(self, new_head: CacheNode) -> None:
        prev_head = self.head.right
        self.head.right = new_head
        new_head.left = self.head
        new_head.right = prev_head
        prev_head.left = new_head
    
    def remove_node(self, node:CacheNode) -> None:
        nleft, nright = node.left, node.right
        nleft.right = nright
        nright.left = nleft

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        self.remove_node(self.nodes[key])
        self.insert_node(self.nodes[key])
        return self.nodes[key].val

    def put(self, key: int, value: int) -> None:
        node = CacheNode(key, value)
        self.nodes[key] = node
        self.insert_node(node)
        if len(self.nodes) > self.capacity:
            lru = self.tail.left
            self.remove_node(lru)
            del self.nodes[lru.key]
