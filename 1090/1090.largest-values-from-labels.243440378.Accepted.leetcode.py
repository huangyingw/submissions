class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        result, used = 0, 0
        remaining = {}
        for value, label in sorted(zip(values, labels), reverse=True):
            remain = remaining.get(label, use_limit)
            if remain > 0:
                result += value
                remaining[label] = remain - 1
                used += 1
                if used == num_wanted:
                    break
        return result
