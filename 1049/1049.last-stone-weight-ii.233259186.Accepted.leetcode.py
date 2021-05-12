class Solution(object):
    def lastStoneWeightII(self, stones):
        all_sums = {0}
        for stone in stones:
            all_sums |= {stone + prev_sum for prev_sum in all_sums}
        return min(abs(sum(stones) - s - s) for s in all_sums)
