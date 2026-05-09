class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = list(set(nums))
        nums.sort() #nlgn
        i = 0
        mx = 1
        current = 1
        while i + 1 < len(nums):
            if nums[i+1] == nums[i] + 1:
                current +=1
            else:
                mx = max(current, mx)
                current = 1
            i+=1
        # Corner Case
        # We reached end while finding largest consecutive
        mx = max(current, mx)
        return mx
# Time Complexity: O(nlgn)
# Space Complexity: O(n)


# Followup
# Do it in linear time complexity

#interesting approach, we don't care about positional info at all, also about duplicates either
# ALl we care is do our previous element and post element is here ?
# To reduce repetitive competition, we mark each element visited
# There is a zone (a local block of consecutive) concept here, by growing, we encounter any number in the zone we explore them all
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        visited = set()

        mx = 1
        for num in nums:
            # seems a bit un phytonic but trust me this is the only way
            # We can not use list comprehension/any lazy iterators
            # As we modify the set while inside the loop
            if num not in visited:
                num_left = num - 1
                num_right = num + 1
                left = 0
                right = 0
                # We don't need to check num_left and num_right if they are visited
                # Remember about the zone, if we encounter one we visit all
                # So yeah, we are here means none of the elem in zone is visited
                # But we do add them inside the while loop. Hope makes sense
                while num_left in nums:
                    left += 1
                    visited.add(num_left)
                    num_left = num_left - 1
                while num_right in nums:
                    right += 1
                    visited.add(num_right)
                    num_right = num_right + 1
                mx = max(mx, left + right + 1)
        return mx
    # Time complexity: O(n). But one catch, set is a variant of dict, uses hashtable with chaining.
    # In theory, we can have numbers that all collides in same hash, effectively becoming a linked list
    # And having O(n^2). This is in pure theory, it's possible. But rarely collision happens in real life.

    # Space complexity: O(n) -> intermediate set
