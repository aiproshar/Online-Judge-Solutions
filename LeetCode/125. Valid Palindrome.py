
# Basic string operation using list comprehension
# Map to ower char, filter to get rid of non-alphanumeric
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num = [
            item.lower() #map function
            for item in s
            if ord("a") <= ord(item.lower()) <= ord("z") or ord("0") <= ord(item.lower()) <= ord("9") # filter function
        ]
        if alpha_num == alpha_num[::-1]:
            return True
        return False

# Time and space complexity: O(n)


# More pythinic implementation, using linear additional space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num = [x.lower() for x in s if x.isalnum()]
        return  alpha_num == alpha_num[::-1]


## Followup ? Can we do it inplace
# Two pointer approach, we compare if both alphanumeric, else we move pointers next location

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i+=1
            if not s[j].isalnum():
                j-=1
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i+=1
                    j-=1
                else:
                    return False
        return True
# Time complexity: O(n)
# Space complexity: O(1)