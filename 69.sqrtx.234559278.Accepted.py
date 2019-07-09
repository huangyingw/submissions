class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
                    """

        def newton(a, x):

            fA = a * a - x
            if(abs(fA) < 1):
                return a

            b = fA - (2 * a) * a
            return newton(-1 * b / (2 * a), x)
        return int(newton(1.0, x))
