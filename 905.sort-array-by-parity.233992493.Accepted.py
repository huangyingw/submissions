









class Solution(object):
    def sortArrayByParity(self, A):

        return [num for num in A if num % 2 == 0] + [num for num in A if num % 2 == 1]
