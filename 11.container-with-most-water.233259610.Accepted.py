_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = (right - left) * min(height[right], height[left])
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, (right - left) * min(height[right], height[left]))
        return max_area
