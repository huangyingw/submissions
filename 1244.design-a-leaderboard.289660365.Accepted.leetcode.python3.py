from collections import defaultdict
import heapq
class Leaderboard(object):
    def __init__(self):
        self.user_score = defaultdict(int)
    def addScore(self, playerId, score):
        self.user_score[playerId] += score
    def top(self, K):
        return sum(heapq.nlargest(K, self.user_score.values()))
    def reset(self, playerId):
        del self.user_score[playerId]
