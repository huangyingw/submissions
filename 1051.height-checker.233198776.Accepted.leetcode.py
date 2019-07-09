


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        result = 0
        for new_h, hei in zip(heights, sorted(heights)):
            if new_h != hei:
                result += 1
        return result
