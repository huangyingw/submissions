

class Solution:

    def numJewelsInStones(self, J, S):

        ret = 0
        for i in J:
            ret += S.count(i)
        return ret
