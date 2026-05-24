# It felt like leetcode hard
# Binary Search with upper Bound

class TimeMap:

    def __init__(self):
        self.data = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        nums = self.data[key]
        if nums == []:
            return ""
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2

            if timestamp >= nums[mid][1]:
                lo = mid
            else:
                hi = mid - 1
        if timestamp < nums[lo][1]:
            return ""
        return nums[lo][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)