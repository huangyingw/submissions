


class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        result = ''
        if A > B:
            while B > 0 and A > 0:
                if A - B >= 3:
                    if A > 1:
                        result += 'aab'
                        A -= 2
                    else:
                        result += 'ab'
                        A -= 1
                    B -= 1
                else:
                    result += 'ab'
                    A -= 1
                    B -= 1
            if A > 0:
                result += 'a' * A
            if B > 0:
                result += 'b' * B
        else:
            while B > 0 and A > 0:
                if B - A >= 3:
                    if B > 1:
                        result += 'bba'
                        B -= 2
                    else:
                        result += 'ba'
                        B -= 1
                    A -= 1
                else:
                    result += 'ba'
                    A -= 1
                    B -= 1
            if A > 0:
                result += 'a' * A
            if B > 0:
                result += 'b' * B
        return result
