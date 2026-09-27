

'''
Brute Force Approach
'''

class Solution:

    def __init__(self, w: list[int]):

        self.lst = []

        for i in range(len(w)):
            freq = w[i]
            for _ in range(freq):
                self.lst.append(i)

    def pickIndex(self) -> int:

        random_idx = random.randint(0, len(self.lst) - 1)
        return self.lst[random_idx]

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()