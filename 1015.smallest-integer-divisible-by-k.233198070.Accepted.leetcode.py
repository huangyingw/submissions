class Solution(object):
    def smallestRepunitDivByK(self, K):
        length, value = 0, 0
        for no_one in range(100000):
            value = (10 * value + 1) % K
            length += 1
            if value == 0:
                return length
        return -1
