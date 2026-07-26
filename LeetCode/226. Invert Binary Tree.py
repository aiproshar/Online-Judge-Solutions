# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
Recursive Approach:
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# Time Complexity: O(n)
# Space: O(h) recursion depth, which ranges from log2n to n

'''
preorder traversal using stack
No risk of stack overflow
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node is None:
                continue
            node.left, node.right = node.right, node.left
            stack.append(node.right)
            stack.append(node.left)
        return root
# Time Complexity: O(n)
# Space: O(h) which ranges from log2n to n