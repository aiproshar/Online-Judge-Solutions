# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# Simple tree problem, we are using non-local variable aka global variable
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def traverse(node) -> int:
            nonlocal is_balanced
            if is_balanced is False:
                return 0
            if node is None:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            if abs(left - right) > 1:
                is_balanced = False
            return max(left, right) + 1
        traverse(root)
        return is_balanced
# Time Complexity: O(n)
# Space Complexity: O(h)






'''
AI suggestion, avoiding non-local values
Neat and smart, although not sure how much of an impact it will be
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(node) -> int:
            if node is None:
                return 0
            left = traverse(node.left)
            if left == -1:
                return -1
            right = traverse(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return traverse(root) != -1