import collections


class Solution(object):
    def repeatedNTimes(self, A):
        counter = collections.Counter(A)
        return counter.most_common(1)[0][0]
