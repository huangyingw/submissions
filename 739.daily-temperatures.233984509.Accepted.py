_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def dailyTemperatures(self, temperatures):

        result = [0 for _ in range(len(temperatures))]
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, prev_i = stack.pop()
                result[prev_i] = i - prev_i
            stack.append((temp, i))
        return result
