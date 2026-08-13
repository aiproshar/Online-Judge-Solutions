
'''
event sweep interval with a twist
'''
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        events = []
        for start, end in flowers:
            events.append((start, 1))
            events.append((end, -1))
        for x in people:
            '''
            This one line is the whole idea here, watch is also a event
            we dont change anyting here, trigger a event so we can peak at current
            Thats how we are able to know all the sparse queries out of 10^9 bruteforce
            '''
            events.append((x, 0))
        '''
        Sorting is the most important part here, for maultiple events that 
        comes up at same time (add, add, add, expire, watch) we want tp
        Add all then watch then let them expire
        We can also use events.append((end + 1, -1)) then we will only have
        to deal with "add: and "watch" events, same stuffs
        '''
        events.sort(key=lambda x: (x[0], -x[1]))
        numbers = defaultdict(int)

        current = 0
        for time, delta in events:
            current += delta
            numbers[time] = max(current, numbers[time])
        ans = [numbers[item] for item in people]
        return ans
# Time Complexity: O(n+m)log(n+m) where n is no of flowers and m in people
# Space: O(n+m) -> total events