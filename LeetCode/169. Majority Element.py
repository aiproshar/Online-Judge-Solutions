
'''
Easy Problem, return most frequent element
So, Build a frequency dict and return max
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        current_num = nums[0]
        weight = 1

        for i in range(1, len(nums)):
            if nums[i] == current_num:
                weight += 1
            else:
                weight -= 1
                if weight == 0:
                    current_num = nums[i]
                    weight = 1
        return current_num
# Time Complexity: O(n)
# Space Complexity: O(n)

'''
Followup, what if we want to do this in constant space?
This is a quick trick, and only works if max_freq > n//2, means strictly more than half not even half

Vote count, if a specific vote can cancel out others and one has > n//2 votes, means if all other combines they
cannot beat the majority
x: 30 , a:20, b:10, c:10 -> In this scenario this algo will not work. Because if a,b,c teams up x looses
x:100 -> Then only this works

'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Start by assuming the first element is the majority candidate.
        # `weight` tracks the candidate's net lead over everything else seen so far.
        current_num = nums[0]
        weight = 1

        # Scan the rest of the array, updating the candidate as votes cancel out.
        for i in range(1, len(nums)):
            if nums[i] == current_num:
                # Same as candidate: one more vote "for" it.
                weight += 1
            else:
                # Different element: cancel one vote (pair it off against the candidate).
                weight -= 1
                # Lead is fully cancelled — the elements so far have tied.
                # Safely adopt the current element as the new candidate.
                if weight == 0:
                    current_num = nums[i]
                    weight = 1

        # The true majority (>n/2 occurrences) can never be fully cancelled,
        # so it's whatever candidate survives to the end.
        return current_num