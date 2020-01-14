from collections import defaultdict
class Solution(object):
    def findShortestSubArray(self, nums):
        counts, limits = defaultdict(int), {}
        for i, num in enumerate(nums):
            counts[num] += 1
            if num not in limits:
                limits[num] = [i, i]
            else:
                limits[num][-1] = i
        max_count, max_nums = 0, []
        for num, count in counts.items():
            if count == max_count:
                max_nums.append(num)
            elif count > max_count:
                max_nums = [num]
                max_count = count
        shortest = float("inf")
        for num in max_nums:
            shortest = min(shortest, limits[num][1] - limits[num][0] + 1)
        return shortest
