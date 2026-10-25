# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def buildTree(i, j) -> TreeNode:
            if i > j:
                return None

            mid = (i + j + 1) // 2

            node = TreeNode(val=nums[mid])

            node.left = buildTree(i, mid - 1)
            node.right = buildTree(mid + 1, j)

            return node

        return buildTree(0, len(nums) - 1)

# Time Complexity: O(n)
# Space Complexity: O(h), h = logN for balanced binary tree

