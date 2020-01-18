class Solution(object):
    def thirdMax(self, nums):
        maxima = [float("-inf")] * 3
        for num in nums:
            if num in maxima:
                continue
            if num > maxima[0]:
                maxima = [num] + maxima[:2]
            elif num > maxima[1]:
                maxima[1:] = [num, maxima[1]]
            elif num > maxima[2]:
                maxima[2] = num
        return maxima[2] if maxima[2] != float("-inf") else maxima[0]
