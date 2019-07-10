class Solution(object):
    def kEmptySlots(self, flowers, k):
        n = len(flowers)
        days = [None for _ in range(n)]
        for day, pos in enumerate(flowers, 1):
            days[pos - 1] = day
        left, right = 0, k + 1
        first_day = n + 1
        while right < n:
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i + k + 1
                    break
            else:
                first_day = min(first_day, max(days[left], days[right]))
                left, right = right, right + k + 1
        return -1 if first_day == n + 1 else first_day
