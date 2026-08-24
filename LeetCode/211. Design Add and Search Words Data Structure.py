class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        current = self.trie
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[None] = None

    def __search(self, word, start_, current) -> bool:
        for i in range(start_, len(word)):
            if word[i] == '.':
                for available in current:
                    if available is None:
                        continue
                    if self.__search(word, i + 1, current[available]):
                        return True
                return False
            elif word[i] not in current:
                return False
            current = current[word[i]]
        return None in current

    def search(self, word: str) -> bool:
        return self.__search(word, 0, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
'''
Write: O(L) time and O(L) space
search: O(L) with no ., 26^L with .


Total Memory consumption: O(N*L) -> Average Length into total Words
'''


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
