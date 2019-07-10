
class Solution:
    def removeElement(self, nums, val):

        times = nums.count(val)
        while times > 0:
            nums.remove(val)
            times -= 1
        return len(nums)
