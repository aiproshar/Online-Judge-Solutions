'''

Initial Solution, Brute Force logic to Avoid Duplicates

'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = set()

        def backtrack(i, sum_, current):
            if sum_ == target:
                temp = current.copy()
                temp.sort()
                res.add(tuple(temp))
                return
            if sum_ > target or i >= len(candidates):
                return
            # take ith element
            current.append(candidates[i])
            backtrack(i + 1, sum_ + candidates[i], current)
            current.pop()

            # skip ith element
            backtrack(i + 1, sum_, current)

        backtrack(0, 0, [])

        return [list(x) for x in res]