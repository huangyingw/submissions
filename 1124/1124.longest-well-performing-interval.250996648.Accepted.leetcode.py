class Solution(object):
    def longestWPI(self, hours):
        TIRING = 8
        result = 0
        net_tiring = 0
        first_net_tiring = {}
        for i, day in enumerate(hours):
            net_tiring += 1 if day > TIRING else -1
            if net_tiring > 0:
                result = i + 1
            if net_tiring - 1 in first_net_tiring:
                result = max(result, i - first_net_tiring[net_tiring - 1])
            if net_tiring not in first_net_tiring:
                first_net_tiring[net_tiring] = i
        return result
