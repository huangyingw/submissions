from collections import defaultdict
class Solution:
    def tallestBillboard(self, rods):
        diffs = {0: 0}
        for rod in rods:
            new_diffs = defaultdict(int, diffs)
            for diff, used_len in diffs.items():
                new_diffs[diff + rod] = max(used_len + rod, new_diffs[diff + rod])
                new_diffs[abs(diff - rod)] = max(used_len + rod, new_diffs[abs(diff - rod)])
            diffs = new_diffs
        return diffs[0] // 2
