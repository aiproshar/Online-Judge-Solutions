# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# Simple postorder traversal
# A bit different, path is not forced from leaf to leaf, so we can discard children without any issue
# If a child is not positive no good use taking them
# So, when returning, if any child is negative, we discard it
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -math.inf
        def traverse(node) -> int:
            if node is None:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            left = max(left, 0) # discard if left tree is negative
            right = max(right, 0) # discard if right tree is negative
            nonlocal max_sum
            if node.val + left + right > max_sum:
                max_sum = node.val + left + right
            return max( node.val + left, node.val + right)
        traverse(root)
        return max_sum
# Time Complexity: O(n)
# Space Complexity: O(h)