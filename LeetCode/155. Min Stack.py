
# initial solution was a bit complex, i was storing min index instead of the actual value
# Code: https://leetcode.com/problems/min-stack/submissions/2004094199/

# This is cleaner one, we don't need to store index, we can directly store the value in the tuple
# We just store upto minimum along with values, what's the minimum we seen here, including the val itself

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            if val < self.stack[-1][1]:
                self.stack.append((val, val))
            else:
                self.stack.append((val, self.stack[-1][1]))


    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Time complexity: O(n) -> N operations, each constant time
# Space complexity: O(n) -> N ops can be push type, so stack hold n tuples

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()