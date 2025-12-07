#Classic OOP based problem

class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = {}

        for i in range(1, 501):
            self.follows[i] = {i}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        user_feed = []
        for tweet in reversed(self.tweets):
            if tweet[0] in self.follows[userId]:
                user_feed.append(tweet[1])
                if len(user_feed) == 10:
                    break
        return user_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        return None

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
