# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None: return "N"
        q = deque([root])
        out = ""
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node is None:
                    out += ("" if not out else ",") + "N"
                    continue
                out += ("" if not out else ",") + f"{node.val}"
                q.append(node.left)
                q.append(node.right)
        return out
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N": return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        idx = 1
        while q:
            node = q.popleft()
            if nodes[idx] != "N":
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx += 1
            if nodes[idx] != "N":
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx += 1
        return root