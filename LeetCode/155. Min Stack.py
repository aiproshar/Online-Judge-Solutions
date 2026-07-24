
# initial solution was a bit complex, i was storing min index instead of the actual value
# Code: https://leetcode.com/problems/min-stack/submissions/2004094199/

# This is cleaner one, we don't need to store index, we can directly store the value in the tuple
# We just store upto minimum along with values, what's the minimum we seen here, including the val itself

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if self.stack:
            # We have elements
            item = (value, min(value, self.stack[-1][1]))
            self.stack.append(item)
        else:
            # empty stack
            self.stack.append((value, value))

    def pop(self) -> None:
        # bound check, always must for interview, even leetcode says we won't run pop on empty
        # Maybe throw an exception, talk with interviewer
        # Show real SWE skills FFS
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()