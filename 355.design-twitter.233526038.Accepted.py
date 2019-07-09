_author_ = 'jake'
_project_ = 'leetcode'











from collections import defaultdict
import heapq


class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId].append([-self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
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
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followers[followerId].discard(followeeId)
