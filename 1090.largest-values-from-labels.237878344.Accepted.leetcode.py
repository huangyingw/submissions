class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        sorted_values = sorted([(i, j) for i, j in zip(values, labels)], key=lambda x: x[0] * -1)
        label_used_count = {label: 0 for label in set(labels)}
        result = 0
        for s_v in sorted_values:
            if num_wanted:
                if label_used_count[s_v[1]] < use_limit:
                    result += s_v[0]
                    label_used_count[s_v[1]] += 1
                    num_wanted -= 1
            else:
                break
        return result
