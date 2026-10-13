class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        count = Counter(hand)

        nums = list(count.keys())
        nums.sort()

        for num in nums:
            freq = count[num]
            if freq == 0:
                continue
            for i in range(groupSize):
                if num + i not in count or count[num + i] < freq:
                    return False
                else:
                    count[num + i] -= freq
        return True
# Time: O(nlogn)
# Space Complexity: O(n)