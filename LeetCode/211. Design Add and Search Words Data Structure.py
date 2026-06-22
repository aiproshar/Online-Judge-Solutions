class WordDictionary:

    def __init__(self):
        self.root = {}

    def backtrack(self, word, idx, curr) -> bool:
        if idx == len(word):
            if None in curr:
                return True
            else:
                return False
        if word[idx] in curr:
            return self.backtrack(word, idx + 1, curr[word[idx]])
        if word[idx] == ".":
            for ch in curr:
                if ch is not None and self.backtrack(word, idx + 1, curr[ch]):
                    return True
            return False
        return False

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w in curr:
                curr = curr[w]
            else:
                curr[w] = {}
                curr = curr[w]
        curr[None] = None

    def search(self, word: str) -> bool:
        return self.backtrack(word, 0, self.root)

'''
Write: O(L) time and O(L) space
search: O(L) with no ., 26^L with .


Total Memory consumption: O(N*L) -> Average Length into total Words
'''


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
