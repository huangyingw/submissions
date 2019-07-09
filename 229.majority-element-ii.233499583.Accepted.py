_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cand1, count1 = None, 0
        cand2, count2 = None, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        return [n for n in (cand1, cand2) if nums.count(n) > len(nums) // 3]
