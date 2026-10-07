

'''
Brute Force Approach
'''

class Solution:

    def __init__(self, w: list[int]):

        self.lst = []

        for i in range(len(w)):
            freq = w[i]
            for _ in range(freq):
                self.lst.append(i)

    def pickIndex(self) -> int:

        random_idx = random.randint(0, len(self.lst) - 1)
        return self.lst[random_idx]

'''
Time Complexity: O(1) for each pickIndex call, O(sum(w)) for init
Space: O(sum(w))
'''


'''
Optimal Method
Binary Search
'''

class Solution:

    def __init__(self, w: list[int]):
        nums = []
        nums.append(w[0])
        for i in range(1, len(w)):
            nums.append(nums[-1] + w[i])
        self.nums = nums
        self.mx = nums[-1]

    def pickIndex(self) -> int:
        # not from zero, as this is inclusive we start from 1
        num = random.randint(1, self.mx)
        return bisect_left(self.nums, num)

# Time Complexity: O(len(w)) for init, log(len(w)) for each pickIndex Call
# Space Complexity: O(len(w))