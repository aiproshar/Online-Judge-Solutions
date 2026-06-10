"""
CCG Pattern -> Choices Constrain Goals
We don't care about index, all we care is i don't want duplicate index element
Save all used index in a set and that's enforce our constraints
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        visited = set()

        def backtrack(current=[]):
            # Goal
            if len(current) == len(nums):
                perms.append(current.copy())
                return
            # Choices
            for i in range(len(nums)):
                # Constrains
                # We dont want duplicates, thats the only constraint
                if i in visited:
                    continue
                current.append(nums[i])
                visited.add(i)
                backtrack(current)
                visited.discard(i)
                current.pop()

        backtrack()
        return perms
    # Time Complexity: Depth N -> len(nums), we have n, n-1, n-2, .. 1 choices each level
    # So n*(n-1)*(n-2)* ...2*1 -> n! Wait, in each node we traverse all the elements to find valid index, thats n
    # So time Complexity: O(n * n!)

    # Space Complexity: DFS, so depth its O(n)
    # Auxiliary Space: n! permutation possible, each n length, so O(n * n!)
