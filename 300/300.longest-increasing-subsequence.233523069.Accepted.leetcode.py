class Solution(object):
    def lengthOfLIS(self, nums):

        LIS = []
        for num in nums:
            list_nb = self.binary_search(num, LIS)
            if list_nb == len(LIS) - 1:
                LIS.append(num)
            else:
                LIS[list_nb + 1] = min(num, LIS[list_nb + 1])
        return len(LIS)

    def binary_search(self, num, LIS):
        left, right = 0, len(LIS) - 1
        while left <= right:
            mid = (left + right) // 2
            if num <= LIS[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return right
