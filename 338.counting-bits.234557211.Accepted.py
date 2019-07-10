


class Solution:
    def countBits(self, num):

        output = [0]
        for i in range(1, num + 1):
            output.append(output[i // 2] + (i % 2))
        return output
