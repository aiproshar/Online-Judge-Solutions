# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Same Tree -> extension. If each node match we try to do a full same tree logic
"""
class Solution:
    def isSame(self, p, q) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        que = deque()
        que.append(root)
        # level order traversal
        while que:
            current = que.popleft()
            if self.isSame(current, subRoot):
                return True
            if current.left:
                que.append(current.left)
            if current.right:
                que.append(current.right)
        return False

# Time Complexity: O(M*N) -> M is big tree N is small Tree
# Space Complexity: O(M) -> level order traversal
