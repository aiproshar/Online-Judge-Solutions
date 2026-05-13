#clean and concise approach
# my initial python was messy, handling a lot of edge case and all nested loops
# Initial py solution: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2001103414/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        max_len = 0

        start = 0
        end = 0

        while end < len(s):
            if s[end] not in substr:
                substr.add(s[end])
                end +=1
                max_len = max(max_len, len(substr))
            else:
                substr.remove(s[start])
                start+=1
        return max_len

'''

Lets solve all two pointers with the below template


left = 0
for right in range(n):
    # expand: update state with nums[right]

    while window_invalid:
        # shrink: undo state for nums[left]
        left += 1
    
    # we are here means we are in a valid state
    # update result

'''

def lengthOfLongestSubstring(self, s: str) -> int:
    substr = set()
    max_len = start = 0

    for end in range(len(s)):
        while s[end] in substr:
            substr.discard(s[start])
            start += 1
        substr.add(s[end])
        max_len = max(max_len, end - start + 1)

    return max_len