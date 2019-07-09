


class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        for num in range(1, N + 1):
            binary_str = ''
            while (num != 0):
                binary_str += str(num % 2)
                num /= 2
            reversed_str = binary_str[::-1]
            if reversed_str not in S:
                return False
        return True
