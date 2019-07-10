_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def generate(self, numRows):

        if numRows == 0:
            return []
        pascal = [[1]]
        for i in range(1, numRows):
            pascal.append([1])
            for num1, num2 in zip(pascal[-2][:-1], pascal[-2][1:]):
                pascal[-1].append(num1 + num2)
            pascal[-1].append(1)
        return pascal
