_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        summary = []
        for num in nums:
            if not summary or num > summary[-1][1] + 1:
                summary.append([num, num])
            else:
                summary[-1][1] = num
        result = [str(i) if i == j else str(i) + '->' + str(j) for i, j in summary]
        return result
