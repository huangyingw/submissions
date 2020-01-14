class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        i, j = 0, 0
        m, n = len(slots1), len(slots2)
        slots1.sort()
        slots2.sort()
        while i < m and j < n:
            latest_start = max(slots1[i][0], slots2[j][0])
            overlap = min(slots1[i][1], slots2[j][1]) - latest_start
            if overlap >= duration:
                return [latest_start, latest_start + duration]
            if slots1[i][0] <= slots2[j][0]:
                i += 1
            else:
                j += 1
        return []
