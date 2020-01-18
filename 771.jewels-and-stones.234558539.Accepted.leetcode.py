class Solution:
    def numJewelsInStones(self, J, S):
        summ = 0
        for i in J:
            summ += S.count(i)
        return summ
