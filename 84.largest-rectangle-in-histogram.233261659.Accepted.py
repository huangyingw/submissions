










class Solution(object):
    def largestRectangleArea(self, heights):

        max_area = 0
        heights = [0] + heights + [0]
        stack = [0]
        for i, bar in enumerate(heights[1:], 1):
            while heights[stack[-1]] > bar:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
