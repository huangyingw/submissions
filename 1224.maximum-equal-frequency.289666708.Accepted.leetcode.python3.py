from collections import defaultdict
class Solution(object):
    def maxEqualFreq(self, nums):
        num_to_count, count_of_counts = defaultdict(int), defaultdict(int)
        result = 0
        max_count = 0
        for i, num in enumerate(nums):
            count = num_to_count[num] + 1
            num_to_count[num] = count
            max_count = max(max_count, count)
            if count != 1:
                count_of_counts[count - 1] -= 1
            count_of_counts[count] += 1
            if max_count == 1:
                result = i + 1
            elif count_of_counts[max_count - 1] == len(num_to_count) - 1:
                result = i + 1
            elif count_of_counts[max_count] == len(num_to_count) - 1 and count_of_counts[1] == 1:
                result = i + 1
        return result
