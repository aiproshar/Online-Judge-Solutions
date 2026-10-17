from functools import cmp_to_key


class Solution:

    def compare(self, a: str, b: str) -> int:
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0

    def largestNumber(self, nums: list[int]) -> str:

        nums = [str(x) for x in nums]
        nums.sort(key=cmp_to_key(self.compare))

        res = "".join(nums)
        if int(res) == 0:
            return "0"
        else:
            return res


# Important Problem
# Special Case where we need cmp_to_key function
