_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def solveEquation(self, equation):

        x, val = 0, 0
        base = 1
        i = 0
        while i < len(equation):
            neg = base
            if equation[i] == "+":
                i += 1
            if equation[i] == "-":
                neg = -base
                i += 1
            num = None
            while i < len(equation) and "0" <= equation[i] <= "9":
                if num is None:
                    num = 0
                num = num * 10 + int(equation[i])
                i += 1
            if num is None:
                num = 1
            if i < len(equation) and equation[i] == "x":
                x += num * neg
                i += 1
            else:
                val += num * neg
            if i < len(equation) and equation[i] == "=":
                base *= -1
                i += 1
        if x == 0 and val == 0:
            return "Infinite solutions"
        if x == 0:
            return "No solution"
        return "x=" + str(-val // x)
