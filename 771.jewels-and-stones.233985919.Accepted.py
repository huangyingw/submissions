









class Solution(object):
    def numJewelsInStones(self, J, S):

        return sum(1 for s in S if s in set(J))
