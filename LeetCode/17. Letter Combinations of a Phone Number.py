
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

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
        # Current/state as parameter should always go last
        def backtrack(i, current):

            if i == len(digits):
                res.append("".join(current))
                return

            for char in keypad[digits[i]]:
                current.append(char)
                backtrack(i+1, current)
                current.pop()
            return
        backtrack(0, [])
        return res


# time complexity: O(4^L), this could be 3^L, but we always assume worst
# Space complexity: Depth stack, O(L),  L * 4^L for output array