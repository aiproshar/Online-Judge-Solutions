
"""
Simplified using node, N-Array Tree Structure
dictionary version easier but not generic, generic solutions more preferable
"""

class Node:
    def __init__(self):
        self.childs = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:

        current = self.root
        for ch in word:
            if ch not in current.childs:
                current.childs[ch] = Node()
            current = current.childs[ch]
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        for ch in word:
            if ch not in current.childs:
                return False
            current = current.childs[ch]
        return current.is_end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for ch in prefix:
            if ch not in current.childs:
                return False
            current = current.childs[ch]
        return True


# TC: O(L) for insert/search/prefix, we walk down and extend trie
# SC: O(N*L) -> No of Inserts * Word len upper bound