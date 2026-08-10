'''
Basic Adhoc Implementation of Zigzag Conversion
Nothing Fancy, you need to visualize how the cursor is moving
Corner Case: Double counting of Edge row elements
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        n = len(s)
        rows = [[] for _ in range(numRows)]

        idx = 0
        while idx < n:
            i = 0
            # Going Down
            while i < numRows and idx < n:
                rows[i].append(s[idx])
                i += 1
                idx += 1

            i = numRows - 2
            # Diagonal Up
            while i > 0 and idx < n:
                rows[i].append(s[idx])
                i -= 1
                idx += 1

        combined = []
        for row in rows:
            combined.extend(row)
        return "".join(combined)

# Time Complexity: O(n)
# Space Complexity: O(n), if numRows > O(n) we have a bunch of empty overhead list lying.