# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




# simple BFS
# On a tree, so there is no cycle and we don't need to do extra stuff to avoid cycle
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        que = deque()
        que.append(root)
        res = []
        while que:
            width = len(que)
            current = []
            for _ in range(width):
                node = que.popleft()
                current.append(node.val)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            res.append(current)
        return res

# Time Complexity: O(n)
# Space complexity: O(n) -> Leaf max width, which on a balanced tree is n/2 nodes means O(n)