class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)

        for num in nums:
            count[num] +=1
            if count[num] > 1:
                return True
        return False


# Using build in counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        # Key is item, value is freq
        for _,val in freq.items():
            if val > 1:
                hash()
                return True

        return False