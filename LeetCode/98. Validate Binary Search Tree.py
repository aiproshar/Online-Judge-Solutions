# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Fail Fast method, as soon as we reach a mismatch, we return
A bit messy code, but okay
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        vals = [-math.inf]

        def dfs(node) -> bool:
            if node is None:
                return True
            if dfs(node.left) is False:
                return False
            if vals[-1] >= node.val:
                return False
            vals.append(node.val)
            if dfs(node.right) is False:
                return False
            return True

        return dfs(root)
# Time Complexity: O(n)