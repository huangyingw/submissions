from fractions import Fraction


class Solution:
    def isRationalEqual(self, S, T):
        def to_numeric(s):
            if not ("(") in s:
                return Fraction(s)
            non_repeat, repeat = s.split("(")
            repeat = repeat[:-1]
            _, non_repeat_decimal = non_repeat.split(".")
            fract = Fraction(int(repeat), (10 ** len(repeat) - 1) * (10 ** len(non_repeat_decimal)))
            return Fraction(non_repeat) + fract
        return to_numeric(S) == to_numeric(T)
