_author_ = 'jake'
_project_ = 'leetcode'




















class Solution:
    def threeEqualParts(self, A):

        one_count = sum(A)
        if one_count == 0:
            return [0, 2]
        ones_per_part, remainder = divmod(one_count, 3)
        if remainder != 0:
            return [-1, -1]
        first_start = 0
        while A[first_start] == 0:
            first_start += 1
        first_end = first_start
        count = 1
        while count < ones_per_part:
            first_end += 1
            count += A[first_end]
        length = first_end - first_start + 1
        second_start = first_end + 1
        while A[second_start] == 0:
            second_start += 1
        if A[first_start:first_end + 1] != A[second_start:second_start + length]:
            return [-1, -1]
        third_start = second_start + length
        while A[third_start] == 0:
            third_start += 1
        if A[first_start:first_end + 1] != A[third_start:third_start + length]:
            return [-1, -1]
        trailing_zeros = len(A) - third_start - length
        first_end += trailing_zeros
        second_end = second_start + length - 1 + trailing_zeros
        if second_start < first_end + 1 or third_start < second_end + 1:
            return [-1, -1]
        return [first_end, second_end + 1]
