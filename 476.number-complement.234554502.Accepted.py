


class Solution(object):
    def findComplement(self, num):
        return int("".join(['1' if i == '0' else '0' for i in bin(num)[2:]]), 2)
