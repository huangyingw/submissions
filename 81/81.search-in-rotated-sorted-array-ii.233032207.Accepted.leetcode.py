class Solution(object):
    def search(self, nums, target):

        def get(start, end):
            if start > end:
                return False
            mid = (start + end) // 2

            while mid < end and nums[mid + 1] == nums[mid]:
                mid += 1
            while start < mid and nums[start + 1] == nums[start]:
                start += 1
            if nums[mid] == target:
                return True
            elif mid == end:
                return get(start, mid - 1)
            elif start == mid:
                return get(mid + 1, end)
            elif nums[mid] >= nums[start]:

                if target >= nums[start] and target < nums[mid]:
                    return get(start, mid - 1)
                else:
                    return get(mid + 1, end)
            elif nums[mid] <= nums[end]:

                if target > nums[mid] and target <= nums[end]:
                    return get(mid + 1, end)
                else:
                    return get(start, mid - 1)
        return get(0, len(nums) - 1)
