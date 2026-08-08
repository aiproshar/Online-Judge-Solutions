# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Recursive DFS, preorder traversal
'''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        def dfs(x: TreeNode, y: TreeNode) -> bool:
            if not x and not y:
                return True
            if not x or not y:
                return False
            if x.val != y.val:
                return False
            return all([
                dfs(x.left, y.right),
                dfs(x.right, y.left)
            ])
        return dfs(root.left, root.right)


# Time Complexity: O(n)
# Space:   logn <= O(h)  <= n, call stack overflow risk

'''
Iterative Preorder Traversal solution
Manual Call stack
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        stack = []
        stack.append((root.left, root.right))

        while stack:
            x, y = stack.pop()
            if not x and not y:
                continue
            if not x or not y:
                return False
            if x.val != y.val:
                return False
            stack.append((x.left, y.right))
            stack.append((x.right, y.left))
        return True
# Time Complexity: O(n)
# Space: O(h), no risk of callstack overflow