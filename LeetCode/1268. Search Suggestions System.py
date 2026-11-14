'''
Trie Based Solution
Bombed AWS PS because i forgot Trie Implementation, came up with Trie Code Very last Moment but there was no
time to code BFS part


BFS bases solution, not optimal
Because we wanr lexio ordering, shorter order is not optimal, we want closest match
'''

class Node:
    def __init__(self, key=None, parent=None):
        self.key = key
        self.parent = parent
        self.is_end = False
        self.childs = {}

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:

        root = Node()
        for product in products:
            current = root
            for ch in product:
                if ch not in current.childs:
                    current.childs[ch] = Node(ch, current)
                current = current.childs[ch]

            # End of Word marker
            current.is_end = True

        res = []

        def find_words(word: str) -> list[str]:
            current = root
            for ch in word:
                if ch not in current.childs:
                    return []
                else:
                    current = current.childs[ch]
            que = deque([current])
            output = []
            while que:
                node = que.popleft()
                # EOF NODE
                if node.is_end is True:
                    current = node
                    path = []
                    while current.key is not None:
                        path.append(current.key)
                        current = current.parent
                    path.reverse()
                    output.append("".join(path))
                for child_key in sorted(node.childs.keys()):
                    que.append(node.childs[child_key])
            return sorted(output)[0:3]

        word = ""
        for ch in searchWord:
            word = word + ch
            res.append(find_words(word))

        return res



'''
DFS based solution and this is more perfect
DFS run on each word
SO when we hit end we store word at that node
'''

class Node:
    def __init__(self, key=None, parent=None):
        self.childs = {}
        self.word = None


class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:

        root = Node()
        # lexigraphically insertion order
        products.sort()
        for product in products:
            current = root
            for ch in product:
                if ch not in current.childs:
                    current.childs[ch] = Node(ch, current)
                current = current.childs[ch]

            # End of Word marker
            current.word = product

        def dfs(node: Node, out: list[str]):
            if len(out) == 3:
                return
            if node.word is not None:
                out.append(node.word)
            for child in sorted(node.childs):
                dfs(node.childs[child], out)

        res = []
        current = root
        for ch in searchWord:
            if current is None or ch not in current.childs:
                res.append([])
                current = None
            else:
                current = current.childs[ch]
                out = []
                dfs(current, out)
                res.append(out)
        return res


'''
Binary Search Based solution
'''
class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:

        products.sort()
        res = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            idx = bisect.bisect_left(products, prefix)
            current_match = []
            for i in range(idx, idx + 3):
                if i == len(products):
                    break
                if products[i].startswith(prefix):
                    current_match.append(products[i])
                else:
                    break
            res.append(current_match)
        return res

# Time Complexity: O(nlogn + m * logn), n = no of products, m = len of search word
# Space: O(m)