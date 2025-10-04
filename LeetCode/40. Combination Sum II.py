

# Unoptimized
# We check for duplicates before each append
# list -> sort -> convert to tuple -> check in set
# 2^N leaf nodes with sorting overhead -> 2^NlogN, bad AF
class Solution:

    def dfs(self, path, path_sum, idx):
        if path_sum == self.target:
            self.combination.append(path[:])
            return
        if path_sum > self.target or idx >= len(self.candidates):
            return
        path.append(self.candidates[idx])
        self.dfs(path, path_sum + self.candidates[idx], idx)

        path.pop()
        self.dfs(path, path_sum, idx + 1)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.candidates = candidates
        self.combination = []
        self.dfs([], 0, 0)
        return self.combination


# Whatever we do, we must explore all possible combinations
# So the best time complexity we can get is 2^N, that means we must get rid of this duplicate checking
# 3 sum -> we did something similar, we sorted the array do do fast invalidation
# same here, while loop continue iteration while nums[index+1] == nums[index]

class Solution:
    def dfs(self, idx, path, path_sum):

        # Termination Check
        if path_sum == self.target:
            path_new = path[:]
            path_new.sort()
            path_new = tuple(path_new)
            if path_new not in self.unique:
                self.unique.add(path_new)
                self.answer.append(path[:])
            return
        if path_sum > self.target or idx == len(self.candidates):
            return
        
        # Branch Out

        #Take the current element
        path.append(self.candidates[idx])
        self.dfs(idx + 1, path, path_sum + self.candidates[idx])

        #skip the current element, and all current element alike
        path.pop()

        '''
        We make a subtle change here
        '''
        while idx + 1 < len(self.candidates) and self.candidates[idx + 1] == self.candidates[idx]:
            idx += 1
        self.dfs(idx + 1, path, path_sum)


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.candidates = candidates
        '''
        Also sort the array, prerequisite
        '''
        self.candidates.sort()
        self.answer = []

        self.unique = set([])

        self.dfs(0, [], 0)

        return self.answer



        
