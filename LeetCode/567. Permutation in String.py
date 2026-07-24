"""
Quite Complex for a medium problem
Anagrams + sub-string problem

Fixed Window sliding Problem, cleaner invariant design
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        freq_s1 = [0] * 26  # constant window
        freq_s2 = [0] * 26  # sliding here.

        for i in range(len(s1)):
            freq_s1[ord(s1[i]) - ord('a')] += 1
            freq_s2[ord(s2[i]) - ord('a')] += 1

        k = len(s1)
        if freq_s1 == freq_s2:
            return True

        # Loop Invariant, we processed upto j length
        for j in range(len(s1), len(s2)):
            freq_s2[ord(s2[j - k]) - ord('a')] -= 1
            freq_s2[ord(s2[j]) - ord('a')] += 1
            if freq_s1 == freq_s2:
                return True
        return False
        return False
# Time complexity: O(n) -> two pointer one pass, honestly its 26* O(n). But we are using array, a so lot of cache hit
# Space complexity: O(1) -> Yes, because keys are constant space, only 26 letter





# O(N) true , no 26
# A bit messy implementation, not super proud, but if works it works
# Code ok but lacks a bit of readability . This problem already complex, now that True O(n) more complexity

from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Single diff map: freq[c] = count_in_window(c) - count_in_s1(c)
        # When freq[c] == 0, character c has a perfect match
        freq = defaultdict(lambda: 0)

        # Build initial window and subtract s1 frequencies
        for char in s2[:len(s1)]:
            freq[char] += 1
        for char in s1:
            freq[char] -= 1

        # Start with 26 (all letters matched) and subtract
        # any character whose diff is non-zero.
        # Characters not in freq are implicitly 0 (already matched).
        match_count = 26
        for _, val in freq.items():
            if val != 0:
                match_count -= 1

        # Check if the first window itself is a permutation
        if match_count == 26:
            return True

        left = 0
        right = len(s1) - 1

        while right + 1 < len(s2):
            # --- Remove left char from window ---
            freq[s2[left]] -= 1
            # If diff just became 0, we gained a match
            if freq[s2[left]] == 0:
                match_count += 1
            # If diff just became -1 (was 0), we lost a match
            elif freq[s2[left]] == -1:
                match_count -= 1

            # --- Add next right char to window ---
            freq[s2[right + 1]] += 1
            # If diff just became 0, we gained a match
            if freq[s2[right + 1]] == 0:
                match_count += 1
            # If diff just became 1 (was 0), we lost a match
            elif freq[s2[right + 1]] == 1:
                match_count -= 1

            if match_count == 26:
                return True

            left += 1
            right += 1

        return False

# Time:  O(n) — single pass with O(1) work per step
# Space: O(1) — freq map bounded by 26 lowercase letters
