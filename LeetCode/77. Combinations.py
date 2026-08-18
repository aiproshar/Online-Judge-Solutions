class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, current):
            if len(current) == k:
                res.append(current.copy())
                return
            # Two exit case
            # one obvious: out of bound
            # second: how many elements we need and we also have
            # if we need 5 elements and have 4 whatever way we go we dont get k elements
            # Off by one corner case, in I state we have not decided to take /skip i yet
            # so n - i + 1 is inclusivae how many we left
            if i > n or n - i  + 1 < k - len(current):
                return
            # take ith element
            current.append(i)
            backtrack(i+1, current)
            current.pop()
            # skip ith element
            backtrack(i+1, current)
        backtrack(1, [])
        return res
# Time: unpruned this is a 2^n take/skip tree.
#   Pruning makes every expanded node feasible -> #nodes = C(n+1,k)-1,
#   plus k-length copy at each of the C(n,k) leaves.
#   => O(k * C(n,k)), optimal (output size).
# Space: O(n) recursion depth -- depth follows i, not len(current),
#   since the skip branch advances i without growing current.
#   (Loop formulation would be O(k).) Output: O(k * C(n,k)).