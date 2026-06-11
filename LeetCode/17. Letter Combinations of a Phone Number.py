
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Early Termination, corner case
        if digits == "":
            return []
        keypad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []

        def backtrack(current=[], idx=0):
            # Goal
            if idx == len(digits):
                res.append("".join(current))
                return
            # Choices +  Constrains, we must take only from digits[idx]
            for char in keypad[digits[idx]]:
                current.append(char)
                backtrack(current, idx + 1)
                current.pop()

        backtrack()
        return res

# time complexity: O(4^L), this could be 3^L but we always assume worst
# Space complexity: Depth stack, O(L)