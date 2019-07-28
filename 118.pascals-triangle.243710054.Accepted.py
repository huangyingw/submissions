class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        pascal = [[1]]
        for i in range(1, numRows):
            pascal += [[1]]
            for num1, num2 in zip(pascal[-2][:-1], pascal[-2][1:]):
                pascal[-1].append(num1 + num2)
            pascal[-1] += [1]
        return pascal
