class Solution:
    def countBits(self, num):
        return [bin(i).count('1') for i in range(num + 1)]


class Solution:
    def countBits(self, num):
        output = [0]
        for i in range(1, num + 1):
            a = output[i / 2] + (i % 2)
            output.append(a)
        return output
