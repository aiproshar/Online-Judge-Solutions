# Great example of monotonic stack
# Monotonically decreasing stack, which empties stack elem one by one on a bigger number which tries to break the property
#
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for idx,temp in enumerate(temperatures):
            if not stack or temp <= stack[-1][1]:
                stack.append((idx, temp))
            else:
                while stack and stack[-1][1] < temp:
                    answer[stack[-1][0]] = idx - stack[-1][0]
                    stack.pop()
                stack.append((idx, temp))
        return answer
# Time complexity: O(n) -> Two loops but one is grown and another is consumed, both linear, and independent
# Space complexity: O(n)  for the stack


# A cleaner approach, loop invariant
'''
for each element:
    while element violates the stack property:
        resolve it
    push element
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            # Loop invariant, fix while monotonic property will be broken upon append
            while stack and temp > stack[-1][1]:
                answer[stack[-1][0]] = idx - stack[-1][0]
                stack.pop()
            # We can insert into stack, it will not break our property
            stack.append((idx, temp))
        return answer