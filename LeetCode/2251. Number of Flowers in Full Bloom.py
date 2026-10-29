
'''
event sweep interval with a twist
'''
class Solution:
    def fullBloomFlowers(
        self, flowers: list[list[int]], people: list[int]
    ) -> list[int]:

        events = []

        for start, end in flowers:
            events.append((start, 1))
            events.append((end, -1))

        for day in people:
            '''
            This one line is the whole idea here: a watch is also an event.
            It doesn't change anything, it just triggers an event so we can
            peek at the current count. That's how we answer sparse queries
            without brute-forcing every day up to 10^9.
            '''
            events.append((day, 0))

        '''
        Sorting is the most important part here. For multiple events that
        happen on the same day (add, add, add, expire, watch), we want to
        add all, then watch, then let them expire.
        Sorting by -delta gives exactly that order: +1, then 0, then -1.
        We could also use events.append((end + 1, -1)), then we'd only have
        to deal with "add" and "watch" events on the same day. Same idea.
        '''
        events.sort(key=lambda x: (x[0], -x[1]))

        blooms = {}
        current = 0
        for day, delta in events:
            current += delta
            '''
            Only record at watch events. By this point all flowers starting
            today have been added and none ending today have expired yet,
            so current is exactly what this person sees.
            '''
            if delta == 0:
                blooms[day] = current

        return [blooms[day] for day in people]

# Time Complexity: O(n+m)log(n+m) where n is no of flowers and m in people
# Space: O(n+m) -> total events