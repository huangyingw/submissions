_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        for i in range(len(x)):

            if i >= 3:

                if x[i - 1] <= x[i - 3] and x[i] >= x[i - 2]:
                    return True
            if i >= 4:

                if x[i - 1] == x[i - 3] and x[i] >= x[i - 2] - x[i - 4]:
                    return True
            if i >= 5:


                if x[i] >= x[i - 2] - x[i - 4] and x[i - 2] > x[i - 4] and x[i - 3] - x[i - 5] <= x[i - 1] <= x[i - 3]:
                    return True
        return False
