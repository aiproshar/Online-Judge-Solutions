class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        ans = []
        carry = 0

        while a or b or carry > 0:
            a_current = int(a.pop()) if a else 0
            b_current = int(b.pop()) if b else 0

            current = a_current + b_current + carry
            carry = 0

            carry = current // 2
            current = current % 2

            ans.append(str(current))

        return "".join(ans[::-1])

# Time Complexity: O(n) -> Len of binary string
# Space Complexity: O(n)