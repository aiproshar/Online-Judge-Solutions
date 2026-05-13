"""
left = 0
for right in range(n):
    # expand: update state with nums[right]

    while window_invalid:
        # shrink: undo state for nums[left]
        left += 1

    # update result
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = defaultdict(lambda: 0)
        max_freq = 0
        max_len = 0
        left = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            if freq[s[right]] > max_freq:
                max_freq = freq[s[right]]
            # We never decrement max_freq when shrinking the window.
            # A stale max_freq only makes the condition more lenient,
            # keeping the window at least as large as the best we've seen.
            # The window can only grow when we find a genuinely higher max_freq,
            # so this never produces a false positive — only skips pointless shrinks.
            while right - left + 1 > max_freq + k:
                freq[s[left]]-=1
                left+=1
            max_len = max(max_len, right - left + 1)
        return max_len
# time complexity: O(n) one pass
# space complexity: O(1) -> WHY ? because we only have 26 unique elements, so its O(26) ->  O(1)
