# combination of both substring and anagram
# A bit complex, needs to define compare of two dict


class Solution:
    # Area of improvement, we're doing repetitive compare lookups of whole dict
    def isSub(self, s1: defaultdict, s2: defaultdict) -> bool:
        for key, val in s1.items():
            if s2[key] != val:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        freq_s1 = defaultdict(lambda: 0)
        freq_s2 = defaultdict(lambda: 0)

        for char in s1:
            freq_s1[char] += 1

        for char in s2[:len(s1)]:
            freq_s2[char] += 1

        if self.isZero(freq_s1, freq_s2):
            return True
        left = 0
        right = len(s1) - 1

        while right + 1 < len(s2):
            freq_s2[s2[left]] -= 1
            freq_s2[s2[right + 1]] += 1
            if self.isSub(freq_s1, freq_s2):
                return True
            left += 1
            right += 1
        return False
# Time complexity: O(n) -> two pointer one pass, honestly its 26* O(n)
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
