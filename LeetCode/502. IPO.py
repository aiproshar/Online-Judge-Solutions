'''

'''
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:

        # Try to take the one with most profit
        # If not possible due to capital shortage, take the next one
        # Keep the skipped ones in a temp, readd as soon as we can have profits again
        # maybe a heap with temp
        # cannot take any due to capital shortage -> Corner Case, early break [inf loop]

        heap = []
        n = len(capital)

        for i in range(len(profits)):
            heapq.heappush(heap, (-profits[i], capital[i]))

        current_cap = w
        while heap and k > 0:
            temp = []
            is_increased = False
            while heap:
                profit, req_cap = heapq.heappop(heap)
                if req_cap <= current_cap:
                    current_cap -= profit
                    k -= 1
                    is_increased = True
                    break
                else:
                    temp.append((profit, req_cap))

            # Not enough capital for any remaining projects
            # Break early
            if is_increased is False:
                break
            while temp:
                heapq.heappush(heap, temp.pop())

        return current_cap

# Time Complexity: O(K * nlogn)
# Space Complexity: O(n)


