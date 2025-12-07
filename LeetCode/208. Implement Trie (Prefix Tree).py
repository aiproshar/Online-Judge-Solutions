class Node:
    def __init__(self):
        self.words = {}
class Trie:

    def __init__(self):
        self.root = Node()
    def insert(self, word: str) -> None:
        current_node = self.root
        i = 0
        while i < len(word):
            if word[i] in current_node.words:
                current_node = current_node.words[word[i]]
                i += 1
            else:
                break
        while i < len(word):
            new_node = Node()
            current_node.words[word[i]] = new_node
            current_node = new_node
            i += 1
        current_node.words['0'] = True


    def search(self, word: str) -> bool:
        current_node = self.root
        for ch in word:
            if ch not in current_node.words:
                return False
            else:
                current_node = current_node.words[ch]
        if '0' in current_node.words:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for ch in prefix:
            if ch not in current_node.words:
                return False
            else:
                current_node = current_node.words[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Time Complexity: Linear
# Space complexity: Number of Nodes, depends on distribution. 