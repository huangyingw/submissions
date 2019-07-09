_author_ = 'jake'
_project_ = 'leetcode'














from collections import defaultdict


class Solution:
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        used_count = {0: 1}
        for song in range(L):
            new_used_count = defaultdict(int)
            for used, count in used_count.items():
                new_used_count[used + 1] += count * (N - used)
                if used > K:
                    new_used_count[used] += count * (used - K)
            used_count = new_used_count
        return used_count[N] % (10 ** 9 + 7)
