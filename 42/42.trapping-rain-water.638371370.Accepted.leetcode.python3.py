class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        result = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                result += (leftMax - height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                result += (rightMax - height[right])
        return result
