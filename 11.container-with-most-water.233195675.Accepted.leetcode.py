class Solution(object):
    def maxArea(self, height):
        left, right, maxArea = 0, len(height) - 1, 0
        while left < right:
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
