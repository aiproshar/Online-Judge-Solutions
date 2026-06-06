# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
straightforward solution, just build a sorted list by traversing a valid bst
Then access kth index element in the list
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            lst.append(node.val)
            traverse(node.right)
        traverse(root)
        return lst[k-1]
# Time Complexity: O(h+k)
# Space Complexity: O(n)

'''
Follow up: How can we do this without the whole array, lesser time complexity
And maybe in iterative way
'''

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        visited = 0
        kth_item = None
        def traverse(node):
            nonlocal visited
            nonlocal kth_item
            if node is None or kth_item is not None:
                return
            traverse(node.left)
            visited += 1
            if visited == k:
                kth_item = node.val
            traverse(node.right)
        traverse(root)
        return kth_item
# Space Complexity: O(h)
'''
Time Complexity: Where this gets interesting, O(h+k) here, its different here. Because we need to free fall on left
side as this is pre-order traversal and then when we come back up in recursion, we stop at k.
This is a bit different than other tree problems
'''