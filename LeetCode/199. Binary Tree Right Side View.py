# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



"""
BFS level order traversal
Just peak the first item before poping
Keep track of size of each level
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        que = deque()
        view = []
        que.append(root)
        while que:
            lvl_size = len(que)
            view.append(que[0].val)
            while lvl_size:
                lvl_size -= 1
                node = que.popleft()
                if node.right:
                    que.append(node.right)
                if node.left:
                    que.append(node.left)
        return view
# Time Complexity: O(n)
# Space Complexity: O(n)




'''
DFS based solution
We just keep track of depth, did we already ppulated this depth ?
ANd try to visit right thats all
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = []
        def traverse(root, depth):
            if root is None:
                return
            if len(view) < depth:
                view.append(root.val)
            traverse(root.right, depth + 1)
            traverse(root.left, depth + 1)
        traverse(root, 1)
        return view

# Time Complexity: O(n0
# Space C0complexity: O(h)