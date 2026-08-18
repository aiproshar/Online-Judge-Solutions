'''

Initial Solution, Brute Force logic to Avoid Duplicates
Backtrack with SET/TUPLE DS to guarantee path uniqueness

This Gets TLE because of no early termination logic
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
# Time Complexity: 2^N * NlogN (NLogN overhead every state because of copy and sort)
# Space Complexity: O(2^N * N) , as we can have 2^N subset, each can have at most N elements.
# If we don't consider output part of SC then O(n) recursion depth




'''
Instead of using set and tuple, we can sort the candidates
IF we take we take, but if we skip we skip all similar elements
By taking only in one branch, we ensure we dont spawn multiple branches with same element
Only one tree path grows to one duplicate, 2 duplicate, and so on..
This is the whole trick



'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def backtrack(i, sum_, current):
            if sum_ == target:
                res.append(current.copy())
                return
            if sum_ > target or i >= len(candidates):
                return

            # take ith element
            current.append(candidates[i])
            backtrack(i + 1, sum_ + candidates[i], current)
            current.pop()

            # skip ith element, also skip the dupes altogether. candidates sorted, they are packed together
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            backtrack(i + 1, sum_, current)

        backtrack(0, 0, [])

        return res

# Time Complexity: 2^N * N (list copy on each state + NLogN initial sort we can discard)
# Space Complexity: O(2^N * N) , as we can have 2^N subset, each can have at most N elements.
# If we don't consider output part of SC then O(n) recursion depth

'''
candidates = [1,1,1,1,4,4,5,5] (sorted), target = 8      +-- take   \-- skip
A skip never lands on another copy: it free-falls to the end of the block.
Blocks: 1s at i=0..3, 4s at i=4..5, 5s at i=6..7.

[] s=0 i=0
+-- 1 s=1 i=1
|   +-- 1,1 s=2 i=2
|   |   +-- 1,1,1 s=3 i=3
|   |   |   +-- 1,1,1,1 s=4 i=4
|   |   |   |   +-- 1,1,1,1,4 s=8            <== SOLUTION
|   |   |   |   \-- skip 4s -> i=6  1,1,1,1 s=4
|   |   |   |       +-- 1,1,1,1,5 s=9        dead
|   |   |   |       \-- i=8                  exhausted
|   |   |   \-- skip 1s -> i=4  1,1,1 s=3
|   |   |       +-- 1,1,1,4 s=7 i=5
|   |   |       |   +-- 1,1,1,4,4 s=11       dead
|   |   |       |   \-- skip 4 -> i=6  1,1,1,4 s=7
|   |   |       |       +-- 1,1,1,4,5 s=12   dead
|   |   |       |       \-- i=8              exhausted
|   |   |       \-- skip 4s -> i=6  1,1,1 s=3
|   |   |           +-- 1,1,1,5 s=8          <== SOLUTION
|   |   |           \-- i=8                  exhausted
|   |   \-- skip 1s -> i=4  1,1 s=2
|   |       +-- 1,1,4 s=6 i=5
|   |       |   +-- 1,1,4,4 s=10             dead
|   |       |   \-- skip 4 -> i=6  1,1,4 s=6
|   |       |       +-- 1,1,4,5 s=11         dead
|   |       |       \-- i=8                  exhausted
|   |       \-- skip 4s -> i=6  1,1 s=2
|   |           +-- 1,1,5 s=7 i=7
|   |           |   +-- 1,1,5,5 s=12         dead
|   |           |   \-- i=8                  exhausted
|   |           \-- i=8                      exhausted
|   \-- skip 1s -> i=4  1 s=1
|       +-- 1,4 s=5 i=5
|       |   +-- 1,4,4 s=9                    dead
|       |   \-- skip 4 -> i=6  1,4 s=5
|       |       +-- 1,4,5 s=10               dead
|       |       \-- i=8                      exhausted
|       \-- skip 4s -> i=6  1 s=1
|           +-- 1,5 s=6 i=7
|           |   +-- 1,5,5 s=11               dead
|           |   \-- i=8                      exhausted
|           \-- i=8                          exhausted
\-- skip 1s -> i=4  [] s=0
    +-- 4 s=4 i=5
    |   +-- 4,4 s=8                          <== SOLUTION
    |   \-- skip 4 -> i=6  4 s=4
    |       +-- 4,5 s=9                      dead
    |       \-- i=8                          exhausted
    \-- skip 4s -> i=6  [] s=0
        +-- 5 s=5 i=7
        |   +-- 5,5 s=10                     dead
        |   \-- i=8                          exhausted
        \-- i=8                              exhausted

51 nodes, 3 results: [1,1,1,1,4], [1,1,1,5], [4,4].
Note there is exactly one node per (multiset, position) pair - no [1,1,4] twice,
even though three different index pairs could have produced it.
'''