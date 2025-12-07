# Extension/ Followup of 78-subsets problem
# We can have duplicates in the list but we dont want duplicate subsets
# Solution: create unique subset signature and use a set to gurantee each lists uniqueness


class Solution:

    def _dfs(self, path, idx):
        if idx == len(self.nums):
            # we are in the leaf
            temp = tuple(sorted(path.copy())). # list unique signature, its order agnostic
            if temp not in self.unique:
                self.unique.add(temp)
                self.subsets.append(path[:])
            return

        
        path.append(self.nums[idx])
        self._dfs(path, idx + 1)
        path.pop()
        self._dfs(path, idx + 1)
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.unique = set()
        self.nums = nums
        self.subsets = []

        self._dfs([], 0)

        return self.subsets
 # time complexity: Branch -> 2, depth -> n, on each node we sort so nlogn, complexity: O(N log N * 2 ^ N)
 # space compexity: O(n)



# More optimized solution
# This is same 3sum strategy, we avoid duplicates by sorting the arrary and moving forward for same consecutive elements
 class Solution:

    def _dfs(self, path, idx):
        if idx == len(self.nums):
            self.subsets.append(path[:])
            return
        path.append(self.nums[idx])
        self._dfs(path, idx + 1)
        path.pop()
        while idx+1 < len(self.nums) and self.nums[idx+1] == self.nums[idx]:
            idx += 1
        self._dfs(path, idx + 1)
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.unique = set()
        self.nums = sorted(nums)
        self.subsets = []

        self._dfs([], 0)

        return self.subsets

# Time complexity: 2^N and for consecutive moving forward, another n, so O(N * 2 ^ N)

        