





class Solution1:
    def findMin(self, nums):

        return min(nums)




class Solution2:
    def findMin(self, nums):

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[mid - 1]:
                return nums[mid]
            else:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return None
