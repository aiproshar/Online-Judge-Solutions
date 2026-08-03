class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        overlaps = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] <= secondList[j][1] and firstList[i][1] >= secondList[j][0]:
                start = max(firstList[i][0], secondList[j][0])
                end = min(firstList[i][1], secondList[j][1])
                overlaps.append([start, end])
            if firstList[i][1] < secondList[j][1]:
                    i += 1
            else:
                j += 1
        return overlaps
# Time Complexity: O(m+n)
# Space Complexity: O(m+n)