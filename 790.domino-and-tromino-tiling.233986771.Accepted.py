













class Solution(object):
    def numTilings(self, N):

        MOD = 10 ** 9 + 7
        prev_tilings, tilings = 0, 1
        prev_one_extra, one_extra = 0, 0
        for _ in range(N):
            next_tilings = (tilings + prev_tilings + prev_one_extra) % MOD
            next_one_extra = (2 * tilings + one_extra) % MOD
            tilings, prev_tilings = next_tilings, tilings
            one_extra, prev_one_extra = next_one_extra, one_extra
        return tilings
