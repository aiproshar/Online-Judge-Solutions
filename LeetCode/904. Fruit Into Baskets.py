'''
non-obvious sliding window problem
Initially did some weird solutions, for example, i did pick two most frequent ones
and then took the freq of first two items

Understanding the problem statement is the actual problem here lol
Coding took 4 minutes, typical variable sliding window problem
Our solution is more general purpose, k = 2 for this problem, can be anything will work
'''


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:

        # dynamic sliding window
        freq = defaultdict(int)
        i = 0
        j = 0
        max_fruits = 0
        k = 2
        while j < len(fruits):
            freq[fruits[j]] += 1
            while len(freq) > k:
                freq[fruits[i]] -= 1
                if freq[fruits[i]] == 0:
                    del freq[fruits[i]]
                i += 1
            max_fruits = max(max_fruits, j - i + 1)
            j += 1

        return max_fruits
# Time Complexity: O(n)
# Space Complexity: O(1) // O(K) but k is a constant