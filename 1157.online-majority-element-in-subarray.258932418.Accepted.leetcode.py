from collections import defaultdict
import bisect
class MajorityChecker(object):
    def __init__(self, arr):
        self.val_to_indices = defaultdict(list)
        for i, val in enumerate(arr):
            self.val_to_indices[val].append(i)
        self.vals = sorted(self.val_to_indices.keys(), key=lambda x: len(self.val_to_indices[x]), reverse=True)
    def query(self, left, right, threshold):
        for val in self.vals:
            if len(self.val_to_indices[val]) < threshold:
                break
            left_i = bisect.bisect_left(self.val_to_indices[val], left)
            right_i = bisect.bisect_right(self.val_to_indices[val], right)
            if right_i - left_i >= threshold:
                return val
        return -1
