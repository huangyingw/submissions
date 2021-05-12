class Solution(object):
    def mctFromLeafValues(self, arr):
        result = 0
        stack = [float('inf')]
        for a in arr:
            while stack[-1] <= a:
                smallest = stack.pop()
                result += smallest * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            result += stack.pop() * stack[-1]
        return result
