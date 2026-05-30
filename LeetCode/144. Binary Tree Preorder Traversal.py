# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
Ez recursive solution
preorder traversal
'''
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        lst = []

        def rec_pre(root):
            if root is None:
                return
            lst.append(root.val)
            rec_pre(root.left)
            rec_pre(root.right)

        rec_pre(root)
        return lst
# Time Complexity: O(n)
# Space Complexity: O(h) , call stack limitation IRL. Some say O(logN) but that's wrong, what is the tree is not balanced
# h can be between logN -> N. lgN: Balanced Tree, N -> A skewed tree, honestly a linkedlist



'''
Instead of using recursion and that call stack, lets use our own call stack
Stack is LIFO order, we want to explore LST first, that's wy insertion order is reversed
python list supports append/pop in the end at O(1), practically a stack lol

'''
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stk = []
        output = []
        stk.append(root)

        while stk:
            node = stk.pop()
            if node is None:
                continue
            else:
                output.append(node.val)
                stk.append(node.right)
                stk.append(node.left)
        return output
# Time Complexity: O(n)
# Space Complexity: O(h) , No call stack risk here. h can be between logN -> N
