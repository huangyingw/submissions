







class Solution(object):
    def diffWaysToCompute(self, input):

        start = 0
        parsed = []
        for i in range(len(input)):
            if not input[i].isdigit():
                parsed.append(int(input[start:i]))
                parsed.append(input[i])
                start = i + 1
        parsed.append(int(input[start:len(input)]))
        return self.diff_ways(parsed, 0, len(parsed) - 1, {})

    def diff_ways(self, s, left, right, memo):
        if left == right:
            return [s[left]]
        if (left, right) in memo:
            return memo[(left, right)]
        ways = []
        for i in range(left + 1, right, 2):
            left_results = self.diff_ways(s, left, i - 1, memo)
            right_results = self.diff_ways(s, i + 1, right, memo)
            for l in left_results:
                for r in right_results:
                    if s[i] == '+':
                        ways.append(l + r)
                    elif s[i] == '-':
                        ways.append(l - r)
                    elif s[i] == '*':
                        ways.append(l * r)
        memo[(left, right)] = ways
        return ways
