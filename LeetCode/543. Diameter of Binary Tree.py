# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



"""
Keep track of two things, first what if the diameter goes through root, and also if not the longest subtree depth
So we consider both thing, imagine that diameter through root, is it max ? compare
maybe the root is somewhere above, pass the max depth
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_len = 0

        def traverse(node) -> int:
            nonlocal max_len
            if node is None:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            # left + right + 1 -> this was my initial mistake, we need to think for a n nodes linkedlist, we have n-1 edges. Each diameter is a linkedlist
            max_len = max(max_len, left + right)
            return max(left, right) + 1
        traverse(root)
        return max_len
# T