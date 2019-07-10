_author_ = 'jake'
_project_ = 'leetcode'
























from collections import Counter
import re


class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):

        class CounterMul(Counter):
            def __add__(self, other):
                self.update(other)
                return self

            def __sub__(self, other):
                self.subtract(other)
                return self

            def __mul__(self, other):
                product = CounterMul()
                for x in self:
                    for y in other:
                        xy = tuple(sorted(x + y))
                        product[xy] += self[x] * other[y]
                return product
        vals = dict(zip(evalvars, evalints))

        def make_counter(token):
            token = str(vals.get(token, token))
            if token.isalpha():
                return CounterMul({(token,): 1})
            return CounterMul({(): int(token)})

        counter = eval(re.sub('(\w+)', r'make_counter("\1")', expression))



        sorted_terms = sorted(counter, key=lambda x: (-len(x), x))
        result = []
        for term in sorted_terms:
            if counter[term]:
                result.append("*".join((str(counter[term]),) + term))
        return result
