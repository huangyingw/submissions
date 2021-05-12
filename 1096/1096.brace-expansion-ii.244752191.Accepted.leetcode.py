class Solution(object):
    def braceExpansionII(self, exp):
        stack = []
        for c in exp:
            if c == "{" or c == ",":
                stack.append(c)
            elif c == "}":
                while stack[-2] == ",":
                    stack[-3] |= stack[-1]
                    stack.pop()
                    stack.pop()
                del stack[-2]
            else:
                stack.append(set(c))
            while len(stack) > 1 and isinstance(stack[-1], set) and isinstance(stack[-2], set):
                second = stack.pop()
                first = stack.pop()
                stack.append(set(w1 + w2 for w1 in first for w2 in second))
        return list(sorted(stack[-1]))
