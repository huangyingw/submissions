class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
    def maximumProduct(self, nums):
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])
    def maximumProduct(self, nums):
        min1 = min2 = 1000
        max1 = max2 = max3 = -1000
        for num in nums:
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
        return max(min1 * min2 * max1, max1 * max2 * max3)
