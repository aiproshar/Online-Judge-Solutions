'''
Advanced Variation of event sweep algorithm
Each event is not only +-1, it has a value associated with itself
Almost 99% same as event sweep, meeting rooms ii
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        events = []

        for people, start, end in trips:
            events.append((start, people))
            events.append((end, -people))
        # We can also remove the lambda, as python default is increasing
        # Corner Case: 4, -7 and 4 10 -> People must get off first, then board
        # Python handles this naturally, because as first values matchd, it moved to second value and luckily its
        # also increasing, means negative events comes first
        # Cople of corner case, like 3 events of boarding at same place, maybe first 2 groups will not cross capacity
        # Adding third will and eventually we will do that
        events.sort(key=lambda x: (x[0], x[1])) #events.sort() also works due to the eay default sorting works
        current_people = 0
        for _, change in events:
            current_people += change
            if current_people > capacity:
                return False
        return True

# Time Complexity: O(nlogn) + bunch of linear scan
# Space Complexity: O(n)
