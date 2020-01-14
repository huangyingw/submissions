class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        temp1, temp2, temp3, temp4 = [], [], [], []
        for i, (a1, a2) in enumerate(zip(arr1, arr2)):
            temp1.append(a1 + a2 + i)
            temp2.append(a1 + a2 - i)
            temp3.append(a1 - a2 + i)
            temp4.append(a1 - a2 - i)
        return max(max(temp) - min(temp) for temp in [temp1, temp2, temp3, temp4])
