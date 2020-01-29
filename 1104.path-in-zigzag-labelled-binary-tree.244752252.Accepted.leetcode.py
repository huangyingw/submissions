class Solution(object):
    def pathInZigZagTree(self, label):
        power_of_2 = 1
        while power_of_2 <= label:
            power_of_2 *= 2
        a = label
        b = power_of_2 - label - 1 + power_of_2 // 2
        result = []
        while a != 1:
            result.append(a)
            a /= 2
            b /= 2
            a, b = b, a
        result.append(1)
        return result[::-1]
