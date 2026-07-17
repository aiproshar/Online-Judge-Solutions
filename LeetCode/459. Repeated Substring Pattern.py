'''
BruteForce Approach
'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:


        for i in range(len(s )//2):

            substr = s[: i +1]
            if len(s) % len(substr) != 0:
                continue
            else:
                if substr * (len(s) // len(substr)) == s:
                    return True
        return False

# Time Complexity: O(n^)
# Space: O(n)