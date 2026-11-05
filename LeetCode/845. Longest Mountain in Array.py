
class Solution:
    def longestMountain(self, arr: list[int]) -> int:

        i = 0
        n = len(arr)
        max_len = 0  # 2
        while i < n - 1:  # 2,1,4,7,3,2,5]

            current_len = 1  #
            ops = [False, False]
            # ascent
            while i + 1 < n and arr[i + 1] > arr[i]:
                ops[0] = True
                i += 1
                current_len += 1
            # descent
            while i + 1 < n and arr[i + 1] < arr[i]:
                ops[1] = True
                i += 1
                current_len += 1

            if ops == [True, True]:
                max_len = max(max_len, current_len)

            # more to furthest on plain
            while i + 1 < n and arr[i + 1] == arr[i]:
                i += 1

        return max_len

# Time Complexity: O(n)
# Space Complexity: O(1)




