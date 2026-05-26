"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Classic Two Pass Algorithm
# One pass generate all the nodes
# Another pass generate all the relations

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        nodes[None] = None

        current_node = head
        while current_node is not None:
            new_node = Node(current_node.val)
            nodes[current_node] = new_node
            current_node = current_node.next

        current_node = head
        while current_node is not None:
            new_node = nodes[current_node]
            new_node.next = nodes[current_node.next]
            new_node.random = nodes[current_node.random]
            current_node = current_node.next

        return nodes[head]

# Time Complexity: O(max(m,n)
# Space Complexity: O(max(m,n)
