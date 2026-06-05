# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solved it while in airport departure lounge
# Initially thought of some complex stuffs like path trailing and validating, all we need to know is current path max
# So in each recursive call we pass the current max, and pass a new updated version (no reference)
# preorder DFS, recursive
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0

        def traverse(node, current_max):
            if node is None:
                return
            if node.val >= current_max:
                nonlocal good_nodes
                good_nodes += 1
            current_max = max(current_max, node.val)
            traverse(node.left, current_max)
            traverse(node.right, current_max)

        traverse(root, root.val)
        return good_nodes
# time complexity: O(n)
# Space complexity: O(h) -> can have call stack overhead



'''
iterative preorder traversal
Has no risk of call stack overflow
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = []
        good_nodes = 0
        stack.append((root, root.val))

        while stack:
            node, current_max = stack.pop()
            if node.val >= current_max:
                good_nodes += 1
                current_max = max(current_max, node.val)
            if node.left is not None:
                stack.append((node.left, current_max))
            if node.right is not None:
                stack.append((node.right, current_max))
        return good_nodes
# Time Complexity: O(n)
# Space Complexity: O(h)