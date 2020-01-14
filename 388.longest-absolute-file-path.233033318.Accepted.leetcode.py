class Solution(object):
    def lengthLongestPath(self, input):
        if not input:
            return 0
        directories = input.split('\n')
        stack = [[-1, 0]]
        result = 0
        for direct in directories:
            n_tabs = direct.count('\t')
            while stack and stack[-1][0] >= n_tabs:
                stack.pop()
            if "." in direct:
                result = max(result, stack[-1][1] + len(direct) - n_tabs)
            stack.append([n_tabs, stack[-1][1] + len(direct) + 1 - n_tabs])
        return result
