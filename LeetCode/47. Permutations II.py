'''
Same as Permutation original, as we have duplicates we use index to check if takesn
instead of the number directly
To handle duplicate store as set. No pruning
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        def backtrack(current, visited):
            if len(current) == n:
                res.add(tuple(current))
                return

            for i in range(n):
                if i not in visited:
                    current.append(nums[i])
                    visited.add(i)
                    backtrack(current, visited)
                    current.pop()
                    visited.remove(i)

        backtrack([], set())
        return [list(x) for x in res]

# Time Complexity: n! * n  ,  Permutation(N,N) == N! and copy overhead
# Space Complexity: n! * n ,  No of permutation * len_of_each


'''
Non Brute Force Option
Only process duplicates moving forward and not backward, left to right strict enforcement
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        def backtrack(current, visited):
            if len(current) == n:
                res.append(current.copy())
                return

            for i in range(n):
                if i not in visited:
                    if i > 0 and i - 1 not in visited and nums[i - 1] == nums[i]:
                        continue
                    current.append(nums[i])
                    visited.add(i)
                    backtrack(current, visited)
                    current.pop()
                    visited.remove(i)

        backtrack([], set())
        return res
# Time Complexity: n! * n  ,  Permutation(N,N) == N! and copy overhead
# Space Complexity: n! * n ,  No of permutation * len_of_each