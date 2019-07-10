class Solution(object):
    def validateStackSequences(self, pushed, popped):
        idx = 0
        stack = []
        l = len(popped)
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1
        return idx == l
