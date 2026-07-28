# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def dfs(node, current_sum) -> bool:
            if node is None:
                return False
            current_sum = current_sum + node.val
            # leaf node
            if node.left is None and node.right is None:
                if current_sum == targetSum:
                    return True
                else:
                    return False
            # non leaf node
            else:
                return any([
                    dfs(node.left, current_sum),
                    dfs(node.right, current_sum)
                    ])
        return dfs(root, 0)
# Time Complexity: O(n) we visit each node
# Space Complexity: O(h) tree depth, range: [log(n), n]