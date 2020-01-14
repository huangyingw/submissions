from itertools import permutations
class Solution(object):
    def largestTimeFromDigits(self, A):
        best_minutes = -1
        for time in permutations(A):
            hours = time[0] * 10 + time[1]
            if hours >= 24:
                continue
            minutes = time[2] * 10 + time[3]
            if minutes >= 60:
                continue
            total_minutes = hours * 60 + minutes
            if total_minutes > best_minutes:
                best_minutes = total_minutes
                best = time
        if best_minutes == -1:
            return ""
        best = [str(x) for x in best]
        return "".join(best[:2]) + ":" + "".join(best[2:])
