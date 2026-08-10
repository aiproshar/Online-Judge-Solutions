'''
Simple Ad hoc Problem
'''
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        total = 0
        i = 1
        while n:
            if n <= 8:
                total += n * i
                n = 0
            else:
                total += 8 * i
                n -= 8
            i += 1
        return total