










from collections import defaultdict
import heapq


class Twitter(object):
    def __init__(self):

        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId, tweetId):

        self.tweets[userId].append([-self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId):

        self.followers[userId].add(userId)
        following = {u for u in self.followers[userId] if self.tweets[u]}
        last_tweet_i = {u: len(self.tweets[u]) - 1 for u in following}
        tweet_heap = [self.tweets[u][last_tweet_i[u]] + [u] for u in following]
        heapq.heapify(tweet_heap)
        feed = []
        while following and len(feed) < 10:
            _, tweetId, u = heapq.heappop(tweet_heap)
            feed.append(tweetId)
            last_tweet_i[u] -= 1
            if last_tweet_i[u] == -1:
                following.remove(u)
            else:
                heapq.heappush(tweet_heap, self.tweets[u][last_tweet_i[u]] + [u])
        return feed

    def follow(self, followerId, followeeId):

        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):

        self.followers[followerId].discard(followeeId)
