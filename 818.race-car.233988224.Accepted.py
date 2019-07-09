_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        min_steps = {0: 0}

        def helper(dist):
            if dist in min_steps:
                return min_steps[dist]
            k = dist.bit_length()
            if 2 ** k - 1 == dist:
                return k
            steps = k + 1 + helper(2 ** k - 1 - dist)
            for j in range(k - 1):
                steps = min(steps, k + j + 1 + helper(dist - 2 ** (k - 1) + 2 ** j))
            min_steps[dist] = steps
            return steps
        return helper(target)
