












class Solution(object):
    def toHex(self, num):

        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32
        result = []
        while num != 0:
            num, digit = divmod(num, 16)
            if digit > 9:
                result.append(chr(ord("a") + digit - 10))
            else:
                result.append(str(digit))
        return "".join(result[::-1])
