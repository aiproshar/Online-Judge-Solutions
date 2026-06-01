# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right







'''
Recursive approach, take max of left and right, add +1 that counts us in
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        mx = max(left, right)
        return mx + 1

'''
level order traversal BFS, take count how many pass we populated the stack
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        que = deque()
        depth = 0
        que.append(root)

        while que:
            nodes_count = len(que)
            depth += 1
            while nodes_count:
                current = que.popleft()
                if current.left != None:
                    que.append(current.left)
                if current.right != None:
                    que.append(current.right)
                nodes_count -= 1
        return depth

# Time complexity: O(n)
# SPace complexity: O(h)







