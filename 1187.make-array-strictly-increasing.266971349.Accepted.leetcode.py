from collections import defaultdict
import bisect
class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        arr2.sort()
        num_to_ops = {-1: 0}
        for num in arr1:
            new_num_to_ops = defaultdict(lambda: float("inf"))
            for prev_num in num_to_ops:
                if num > prev_num:
                    new_num_to_ops[num] = min(new_num_to_ops[num], num_to_ops[prev_num])
                i = bisect.bisect_right(arr2, prev_num)
                if i < len(arr2) and (num <= prev_num or arr2[i] < num):
                    new_num_to_ops[arr2[i]] = min(new_num_to_ops[arr2[i]], num_to_ops[prev_num] + 1)
            num_to_ops = new_num_to_ops
        if num_to_ops:
            return min(num_to_ops.values())
        return -1
