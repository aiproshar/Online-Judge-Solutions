
# Dfs, with alookup table to the next paths
class Solution:
    def dfs(self, path, idx):
        if idx == len(self.digits):
            path_str = ''.join(path)
            if path_str == "":
                return
            self.paths.append(path_str)
            return
        
        for letter in self.mp[self.digits[idx]]:
            path.append(letter)
            self.dfs(path, idx + 1)
            path.pop()
        
    def letterCombinations(self, digits: str) -> List[str]:
        self.mp = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        self.digits = digits
        self.paths = []
        self.dfs([], 0)
        return self.paths

# time complexity: O(4^L), this could be 3^L but we always assume worst
# Space complexity: Depth stack, O(L)