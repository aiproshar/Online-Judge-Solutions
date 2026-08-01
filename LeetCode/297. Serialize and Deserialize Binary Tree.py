# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Recursive preorder DFS traversal
Special marker for None and also String delimiter
Also need to check full empty string, as "" -> will break apart into [""] in split
'''
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if node is None:
                res.append('#')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = deque(data.split(','))

        def dfs(data) -> TreeNode:
            if not data:
                return None
            if data[0] == '#' or data[0] == "":
                data.popleft()
                return None
            node = TreeNode(int(data[0]))
            data.popleft()
            node.left = dfs(data)
            node.right = dfs(data)
            return node

        return dfs(data)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))