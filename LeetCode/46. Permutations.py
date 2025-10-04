
# such a beautiful problem
# We are trying generate tree by positioning first element in N potition
# Second element in N-1 position, we mark all the non occupied pos as None
# When we reached at the end of nums, push that to list and exit (leaf node)
# n * n-1 * n-2 * n-3 .... 2..1 -> n! leaf, in each leaft go travere the loop, so its n*n!. Actually its bit more complex, because we are also doing this in the
# previous levels also
# Space complexity: O(n) -> Max Depth per path, we are exploring on path at a time (dfs)
class Solution:
    def dfs(self, perm, idx):
        if idx == len(self.nums):
            self.allprems.append(perm[:])
            return
        for i in range(len(perm)):
            if perm[i] is None:
                perm[i] = self.nums[idx]
                self.dfs(perm, idx + 1)
                # undo the operation, aka backtrack
                perm[i] = None
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        perm = [None] * len(nums)
        self.allprems = []
        
        
        self.dfs(perm, 0)
        return self.allprems