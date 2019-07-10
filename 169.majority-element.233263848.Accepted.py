








class Solution(object):
    def majorityElement(self, nums):

        count, candidate = 0, None
        for i, num in enumerate(nums):
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate
