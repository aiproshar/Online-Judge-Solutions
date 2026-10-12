
class Solution:
    def checkValidString(self, s: str) -> bool:


        @cache
        def dp(i, open, close):

            if close > open:
                # invalid state
                return False
            if i == len(s):
                # end of string
                return open == close

            if s[i] == "(":
                return dp(i + 1, open + 1, close)
            elif s[i] == ")":
                return dp(i + 1, open, close + 1)
            elif s[i] == '*':
                # We have 3 choices
                # open, close or discard
                res = []
                res.append(dp( i +1, open + 1, close))
                res.append(dp( i +1, open, close + 1))
                res.append(dp( i +1, open, close))
                return any(res)

        return dp(0, 0, 0)

# Time Complexity: O(n^3)
# Space Complexity: O(n^3)

'''
Reducing state space, we dont care how many openings and closing there, we only care about balance
Positive balance we have excessive opening
Negative balance means invalid state, excessive closing, you cannot recover from that
Balance == 0 at end means we have a valid string
'''
class Solution:
    def checkValidString(self, s: str) -> bool:

        @cache
        def dp(i, balance):

            if balance < 0:
                return False
            if i == len(s):
                return balance == 0

            if s[i] == '(':
                return dp(i + 1, balance + 1)
            elif s[i] == ')':
                return dp(i + 1, balance - 1)
            elif s[i] == '*':
                return any([
                    dp(i + 1, balance + 1),
                    dp(i + 1, balance - 1),
                    dp(i + 1, balance)
                ])

        return dp(0, 0)
