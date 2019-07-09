
class Solution:







    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = max(count, i - res - 1)
                res = i
        count = max(count, len(nums) - res - 1)
        return count



    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        count = 0
        for n in nums:
            if n:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
        return max_count








    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = bytearray(nums).split(b'\x00')
        return max([len(i) for i in temp])
