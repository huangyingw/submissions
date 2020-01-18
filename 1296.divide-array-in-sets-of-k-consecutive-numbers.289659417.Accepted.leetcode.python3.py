from collections import Counter


class Solution(object):
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False
        counts = Counter(nums)
        for start_num in sorted(counts.keys()):
            count = counts[start_num]
            if count == 0:
                continue
            for num in range(start_num, start_num + k):
                if num not in counts or counts[num] < count:
                    return False
                counts[num] -= count
        return True
