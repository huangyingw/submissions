


class Solution(object):
    def numPairsDivisibleBy60(self, time):

        d = collections.Counter()
        count = 0
        for t in time:
            count += d[-t % 60]
            d[t % 60] += 1
        return count
