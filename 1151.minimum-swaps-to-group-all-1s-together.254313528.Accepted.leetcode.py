class Solution(object):
    def minSwaps(self, data):
        ones = sum(data)
        window_sum = sum(data[:ones])
        result = ones - window_sum
        for i in range(len(data) - ones):
            window_sum -= data[i]
            window_sum += data[i + ones]
            result = min(result, ones - window_sum)
        return result
