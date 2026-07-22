
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for char in s:
            if char.isalnum():
                lst.append(char.lower())
        if lst == lst[::-1]:
            return True
        else:
            return False


# Time and space complexity: O(n)


# More pythonic implementation, using linear additional space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num = [x.lower() for x in s if x.isalnum()]
        return  alpha_num == alpha_num[::-1]

# Time Complexity: O(n)
# Space Complexity: O(n)


## Followup ? Can we do it inplace
# Two pointer approach, we compare if both alphanumeric, else we move pointers next location

class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
            else:
                # no exclusivity, if none of them is alphanum, we progress both ways
                if not s[i].isalnum():
                    i += 1
                if not s[j].isalnum():
                    j -= 1
        return True
# Time complexity: O(n)
# Space complexity: O(1)