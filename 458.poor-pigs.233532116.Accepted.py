_author_ = 'jake'
_project_ = 'leetcode'















from math import log, ceil


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        rounds = minutesToTest // minutesToDie
        return int(ceil(log(buckets) / log(rounds + 1)))
