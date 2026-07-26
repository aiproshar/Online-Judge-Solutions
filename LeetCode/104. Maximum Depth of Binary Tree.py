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

# Time Complexity: O(n)
# Space Complexity: O(h) recursion depth, can be between n -> lgn

'''
level order traversal BFS, take count how many pass we populated the stack
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        que = deque()
        que.append(root)
        depth = 0
        while que:
            width = len(que) #width of current level
            depth += 1 # the depth we are in, increment on each level
            for _ in range(width):
                node = que.popleft()
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
        return depth

# Time complexity: O(n)
# Space complexity: O(n) // no of leaf nodes for balanced tree is n//2







