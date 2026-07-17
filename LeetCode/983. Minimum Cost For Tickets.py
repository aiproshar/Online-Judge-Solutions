'''
Top Down Recursive Approach
The Hardest part is finding out the exact state, which is current which day i am at
I might or might not travel this day
F(n) -< minimum cost upto this day
'''
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        days_set = set(days)
        @cache
        def dfs(current) -> int:
            # current is the day without a pass, we have 3 options
            if current > days[-1]:
                return 0

            res = []
            if current not in days_set:
            # We are not traveling
                return dfs(current+1)
            # A bit counterintuitive, we're buying pass including today and next n-1 days
            # We need to call the day which is out of pass coverage, so if today is x then x + 7 - 1 + 1 => x + 7 day
            # is the first day without coverage

            res.append(dfs(current + 1) + costs[0])
            res.append(dfs(current + 7) + costs[1])
            res.append(dfs(current + 30) + costs[2])

            return min(res)

        # First day without the pass
        return dfs(days[0])

# Time Complexity: O(max(days) - min(days))
# Space Complexity: O(max(days) - min(days)