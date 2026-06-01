# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# Default recursive solution

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)
        traverse(root)
        return result

# Time Complexity: O(n)
# Space Complexity: O(h) -> Call stack limitation IRL



'''
TO visit a node we need to make sure its lst and rst is visited. How we can have that info
A set, which keep tracks of all the nodes visited, that's how
Also, we mark None node as visited, so we can easily explore the leaf nodes as their both children (NOne nodes) are already visited
Need to handle empty root nodes explicitly
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        visited = {None}
        stack = [root]
        result = []

        while stack:
            if stack[-1].left in visited and stack[-1].right in visited:
                result.append(stack[-1].val)
                visited.add(stack[-1])
                stack.pop()
            else:
                current = stack[-1]
                if current.right is not None:
                    stack.append(current.right)
                if current.left is not None:
                    stack.append(current.left)
        return result
# Time complexity: O(n)
# Space Complexity: O(h) + O(n) -> O(n) ; h -> ranges from logn to n