
class Solution(object):



    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set(nums)
        return sorted(list(a))[-3 if len(a) >= 3 else -1]


    def thirdMax(self, nums):
        if len(nums) < 3:
            return max(nums)
        else:
            newNums = set(nums)
            if len(newNums) < 3:
                return max(newNums)
            else:
                newNums = sorted(newNums)
                return newNums[len(newNums) - 3]
