'''
Simple sliding window problem
'''
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        freq = defaultdict(int)
        i = j = 0
        max_len = 0

        while j < len(s):

            freq[s[j]] += 1
            while freq[s[j]] > 2:
                freq[s[i]] -= 1
                i += 1
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len

# Time Complexity: O(n)
# Space Complexity: O(1), cause n or no of distinct chars is bounded by 26