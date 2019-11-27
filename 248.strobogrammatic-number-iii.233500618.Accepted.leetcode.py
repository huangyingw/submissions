class Solution(object):
    def strobogrammaticInRange(self, low, high):
        max_len, min_len = len(high), len(low)
        low, high = int(low), int(high)
        live_list = ['']
        other_list = ['0', '1', '8']
        strobo_count = 0
        strobo = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        if min_len == 1:
            strobo_count += len([i for i in other_list if low <= int(i) <= high])
        for i in range(2, max_len + 1):
            live_list = [c + r + strobo[c] for r in live_list for c in strobo]
            if min_len < i < max_len:
                strobo_count += len([True for result in live_list if result[0] != '0'])
            elif i == min_len or i == max_len:
                strobo_count += len([True for result in live_list if result[0] != '0' and low <= int(result) <= high])
            live_list, other_list = other_list, live_list
        return strobo_count
