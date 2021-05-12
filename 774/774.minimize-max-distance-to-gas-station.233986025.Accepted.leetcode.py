class Solution(object):
    def minmaxGasDist(self, stations, K):
        distances = [s1 - s2 for s1, s2 in zip(stations[1:], stations)]
        distances.sort(reverse=True)

        def can_minmax_dist(d):
            remaining = K
            for dist in distances:
                if dist < d or remaining < 0:
                    break
                remaining -= int(dist // d)
            return remaining >= 0
        max_d, min_d = distances[0], 0
        while max_d - min_d > 10 ** -6:
            mid = (max_d + min_d) // 2.0
            if can_minmax_dist(mid):
                max_d = mid
            else:
                min_d = mid
        return max_d
