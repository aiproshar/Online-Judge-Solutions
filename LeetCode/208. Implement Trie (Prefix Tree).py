# Simple N array tree logic, we use dictionary to keep track of child
# Key is child identifier, value is another dict from which we can go to child of childs
# Corner Case: TO mark ending of a word, we enter None Key, so after traversing the key you hit a none key, means a word ended there,
# You are not only there because of prefix
# Kind of DFS here, deep dive and find a leaf node.

class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:

        current = self.trie
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        # end marker
        current[None] = None

    def search(self, word: str) -> bool:
        current = self.trie
        for char in word:
            if char not in current:
                return False
            current = current[char]
        # Prefix matched, lets check for end marker
        return None in current

    def startsWith(self, prefix: str) -> bool:
        current = self.trie
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Time Complexity: We can have depth of 2000, each depth we can have 26 choices, but we're only exploring one path
# So its O(n) -> len of string for both insert and search
# Space: For insert, 26^n is our state space, where n is max word len, but in reality, if N is no of words and M is avd length,
# Its O(M*N)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)