'''
Sliding window variation problem
'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if k == 0:
            return 0

        freq = defaultdict(int)

        left = right = 0
        max_len = 0

        for right in range(len(s)):

            # expand
            freq[s[right]] += 1

            # invalid state
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            # valid state
            max_len = max(max_len, right - left + 1)

        return max_len
# Time Complexity: O(n)
# Space Complexity: O(k)