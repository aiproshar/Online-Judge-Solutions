"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        new_nodes = {}
        new_nodes[node] = Node(node.val)

        que = deque()
        que.append(node)

        while que:
            parent = que.popleft()
            for child in parent.neighbors:
                if child not in new_nodes:
                    new_nodes[child] = Node(child.val)
                    que.append(child)
                new_nodes[parent].neighbors.append(new_nodes[child])

        return new_nodes[node]
