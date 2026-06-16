class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True # because we adding 1
        for i in reversed(range(len(digits))):
            if carry:
                digits[i] += 1
                carry = False
            if digits[i] > 9:
                digits[i] = 0
                carry = True

            # Else block is additional optimization
            # Early termination, no overflow this stage and no carry
            # Means even 1ll future digits are 9 we don't care, they just as it is
            else:
                break
        if carry:
            digits.insert(0,1)
        return digits

# Time Complexity: O(n) where n is len of digits
# Space Complexity: O(1) we doing inplace