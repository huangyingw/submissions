class Solution(object):
    def verifyPreorder(self, preorder):
        stack = [float('inf')]
        minimum = float('-inf')
        for value in preorder:
            if value < minimum:
                return False
            while value > stack[-1]:
                minimum = stack.pop()
            stack.append(value)
        return True
