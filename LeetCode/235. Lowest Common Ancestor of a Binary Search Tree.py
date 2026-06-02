# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



"""
This is the BST variant, instead of searching a value we search a range, if our root is in that range we got it

There is another problem, LC 236, which is the same thing but not BST, we need to do path traversal there
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        while root:
            if p.val <= root.val <= q.val:
                return root
            elif root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < q.val and root.val < p.val:
                root = root.right

# Time Complexity: O(n)
# Space: O(1)
