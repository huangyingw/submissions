class Solution(object):
    def parseBoolExpr(self, expression):
        stack = []
        for c in expression:
            if c == "t":
                stack.append(True)
            elif c == "f":
                stack.append(False)
            elif c == ")":
                booleans = set()
                while stack[-1] != "(":
                    booleans.add(stack.pop())
                stack.pop()
                operator = stack.pop()
                if operator == "&":
                    stack.append(all(booleans))
                elif operator == "|":
                    stack.append(any(booleans))
                else:
                    stack.append(not booleans.pop())
            elif c != ",":
                stack.append(c)
        return stack[-1]
