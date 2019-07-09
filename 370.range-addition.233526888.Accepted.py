_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        if length <= 0:
            return []
        shifts = [0] * (length + 1)
        for start, end, inc in updates:
            shifts[start] += inc
            shifts[end + 1] -= inc
        output = [shifts[0]]
        for i in range(1, length):
            output.append(output[-1] + shifts[i])
        return output
