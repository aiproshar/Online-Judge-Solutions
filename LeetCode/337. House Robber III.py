# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        SKIP, ROB = 1, 2
        @cache
        def traverse(node, state):

            if node is None:
                return 0
            res = []
            if state == SKIP:
                # We cannot rob
                res.append(traverse(node.left, ROB) + traverse(node.right, ROB))
            else:
                # AT WILL
                # We decided to skip current house
                res.append(traverse(node.left, ROB) + traverse(node.right, ROB))

                # We decided to rob current house
                res.append(
                    traverse(node.left, SKIP) + traverse(node.right, SKIP) + node.val
                )
            return max(res)
        return traverse(root, ROB)
# Time Complexity: O(n)
# Space Complexity: O(n) + O(h) recursion stack