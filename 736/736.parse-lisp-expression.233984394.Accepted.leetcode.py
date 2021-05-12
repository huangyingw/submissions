class Solution(object):
    def evaluate(self, expression):
        tokens = expression.split(" ")
        scopes = [{}]

        def helper(start):
            if start >= len(tokens):
                return 0, start
            operator = tokens[start]
            if operator[0] == "(":
                operator = operator[1:]
                scopes.append(dict(scopes[-1]))
            closing_brackets = 0
            while operator[len(operator) - 1 - closing_brackets] == ")":
                closing_brackets += 1
            if closing_brackets > 0:
                operator = operator[:-closing_brackets]
            if operator.isdigit() or operator[0] == "-" and operator[1:].isdigit():
                result = int(operator), start + 1
            elif operator == "add":
                left, next_i = helper(start + 1)
                right, next_i = helper(next_i)
                result = (left + right, next_i)
            elif operator == "mult":
                left, next_i = helper(start + 1)
                right, next_i = helper(next_i)
                result = (left * right, next_i)
            elif operator == "let":
                next_i = start + 1
                while continue_let(next_i):
                    variable = tokens[next_i]
                    expression, next_i = helper(next_i + 1)
                    scopes[-1][variable] = expression
                result = helper(next_i)
            else:
                result = (scopes[-1][operator], start + 1)
            while closing_brackets > 0:
                closing_brackets -= 1
                scopes.pop()
            return result

        def continue_let(i):
            return "a" <= tokens[i][0] <= "z" and tokens[i][-1] != ")"
        return helper(0)[0]
