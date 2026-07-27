# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Recursive call on both tree
Are the Nodes Null -> we are Good
Are the nodes null exclusively -> Not good
Are values same
Repeat for child result and if both true we good
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

# Time Complexity: O(n)
# Space Complexity: O(h)


'''
Iterative Approach, no risk of stack overflow
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = []

        stack.append((p, q))
        while stack:
            x, y = stack.pop()
            if x is None and y is None:
                continue
            if x is None or y is None:
                return False
            if x.val != y.val:
                return False
            stack.append((x.left, y.left))
            stack.append((x.right, y.right))
        return True
