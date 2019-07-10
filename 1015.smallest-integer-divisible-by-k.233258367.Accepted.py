











class Solution(object):
    def smallestRepunitDivByK(self, K):

        if K % 10 not in {1, 3, 7, 9}:
            return -1
        mod_N, mod_set = 0, set()
        for length in range(1, K + 1):
            mod_N = (10 * mod_N + 1) % K
            if mod_N == 0:
                return length
            if mod_N in mod_set:
                return -1
            mod_set.add(mod_N)
        return -1
