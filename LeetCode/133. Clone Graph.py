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

        # early termination
        if node is None:
            return None

        mirror = {}
        que = deque()
        que.append(node)
        mirror[node] = Node(node.val)

        while que:
            current = que.popleft()

            for child in current.neighbors:
                if child not in mirror:
                    # brand new child, lets create the mirror and que for further explore
                    mirror[child] = Node(val=child.val)
                    que.append(child)
                # we must create the connection regardless the child was visted before or not
                mirror[current].neighbors.append(mirror[child])

        return mirror[node]

# Time Complexity: O(V+E)
# Space Complexity: O(V+E) in the output, Aux Space is O(V)