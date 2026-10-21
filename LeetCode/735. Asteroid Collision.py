class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        stack = []

        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
            # collision case
            elif stack[-1] > 0 and asteroids[i] < 0:
                current = asteroids[i]
                while stack and stack[-1] > 0 and current < 0:
                    last = stack.pop()
                    if abs(last) > abs(current):
                        current = last
                    elif abs(last) == abs(current):
                        current = 0
                if current != 0:
                    stack.append(current)
            else:
                stack.append(asteroids[i])
        return stack

# Time Complexity: O(n)
# Space Complexity: O(1)