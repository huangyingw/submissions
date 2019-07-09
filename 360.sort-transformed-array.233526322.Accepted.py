_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def transform(x):
            return a * x * x + b * x + c
        transformed = [transform(num) for num in nums]
        left, right = 0, len(nums) - 1
        result = []
        while left <= right:
            if (a > 0 and transformed[left] > transformed[right]) or (a <= 0 and transformed[right] > transformed[left]):
                result.append(transformed[left])
                left += 1
            else:
                result.append(transformed[right])
                right -= 1
        return result[::-1] if a > 0 else result
