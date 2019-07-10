class Solution(object):
    def calculate(self, s):
        operators = {"+", "-", "*", "/"}

        def parse(i):
            parsed = []
            while i < len(s):
                c = s[i]
                if c in operators:
                    parsed.append(c)
                elif "0" <= c <= "9":
                    if parsed and isinstance(parsed[-1], int):
                        parsed[-1] = parsed[-1] * 10 + int(c)
                    else:
                        parsed.append(int(c))
                elif c == "(":
                    sublist, i = parse(i + 1)
                    parsed.append(sublist)
                elif c == ")":
                    return parsed, i
                i += 1
            return parsed, len(s)

        def calculate(tokens):
            if isinstance(tokens, int):
                return tokens
            result = [calculate(tokens[0])]
            for i in range(1, len(tokens), 2):
                op, num = tokens[i], calculate(tokens[i + 1])
                if op == "/":
                    result.append(result.pop() // num)
                elif op == "*":
                    result.append(result.pop() * num)
                elif op == "+":
                    result.append(num)
                else:
                    result.append(-num)
            return sum(result)
        parsed_s, _ = parse(0)
        return calculate(parsed_s)
