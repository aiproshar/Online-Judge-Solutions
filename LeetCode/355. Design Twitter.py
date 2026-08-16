'''
Old Solution was YIKES, It was linear Scan and compare if it's a friend,
It was the dumbest solution

New one uses Heap, so
'''

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)
        self.counter = 0

        for i in range(1, 501):
            self.follows[i].add(i)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        heap = []

        for followed in self.follows[userId]:
            counter = 10
            i = len(self.posts[followed]) - 1
            while i >= 0 and counter >= 0:
                heapq.heappush(heap, self.posts[followed][i])
                if len(heap) > 10:
                    heapq.heappop(heap)
                i -= 1
        tweets = []
        while heap:
            _, tweet = heapq.heappop(heap)
            tweets.append(tweet)
        return tweets[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followeeId:
            self.follows[followerId].discard(followeeId)




'''
A bit better Solution, this is interview ready
Instead of taking 10 elements from each, we early terminate if the oldest post of heap is newer than 
the curren followed post and heap is already at cap

Also we dont to that initial make each friend of themself trick, that's bad according to all AIs
And for x in set_a | set_b # New syntax. So beautful
'''


class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        heap = []

        for followed in self.follows[userId] | {userId}:
            i = len(self.posts[followed]) - 1
            while i >= 0:
                if len(heap) == 10:
                    if self.posts[followed][i][0] > heap[0][0]:
                        heapq.heappush(heap, self.posts[followed][i])
                        heapq.heappop(heap)
                    else:
                        break
                else:
                    heapq.heappush(heap, self.posts[followed][i])
                i -= 1
        tweets = []
        while heap:
            _, tweet = heapq.heappop(heap)
            tweets.append(tweet)
        return tweets[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)