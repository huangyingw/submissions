_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.append(0)
        i = 0
        while n > 0 and i < len(flowerbed) - 1:
            if flowerbed[i + 1] == 1:
                i += 3
            elif flowerbed[i] == 1:
                i += 2
            elif i != 0 and flowerbed[i - 1] == 1:
                i += 1
            else:
                n -= 1
                i += 2
        return n == 0
