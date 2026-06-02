# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Bloated solution
We save the paths to both node using DFS, and then from paths the last match is the lowest common node
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(root, val, path) -> bool:
            if root is None:
                return False
            if root.val == val:
                path.append(root)
                return True
            childs = traverse(root.left, val, path) or traverse(root.right, val, path)
            if childs:
                path.append(root)
                return True
            else:
                return False

        path_p = []
        # Traverse path of P
        traverse(root, p.val, path_p)
        # Traverse path of q
        path_q = []
        traverse(root, q.val, path_q)
        lca = None
        while path_p and path_q and path_p[-1] == path_q[-1]:
            lca = path_p[-1]
            path_p.pop()
            path_q.pop()
        return lca

# Time Complexity: O(n)
# Space Complexity: O(h)



# More straightforward solution, we dont need path
# Keep a counter, when we see p or q increase it and propagate
# First time counter reaches 2 means we have LCA
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = None
        def traverse(root) -> int:
            if root is None:
                return 0
            current = 0
            if root is p or root is q:
                current = 1
            left = traverse(root.left)
            right = traverse(root.right)
            if current + left + right == 2:
                nonlocal ancestor
                if ancestor is None:
                    ancestor = root
            return current + left + right

        traverse(root)
        return ancestor

# Time Complexity: O(n)
# Space Complexity: O(h)
