# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




# simple BFS
# On a tree, so there is no cycle and we don't need to do extra stuff to avoid cycle
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        output = []
        que = deque()
        que.append(root)
        while que:
            current_len = len(que)
            level_out = []
            while current_len > 0:
                current = que.popleft()
                level_out.append(current.val)
                if current.left is not None:
                    que.append(current.left)
                if current.right is not None:
                    que.append(current.right)
                current_len -= 1
            output.append(level_out)
        return output

# Time Complexity: O(n)
# Space complexity: O(n) -> Leaf max width, which on a balanced tree is n/2 nodes means O(n)