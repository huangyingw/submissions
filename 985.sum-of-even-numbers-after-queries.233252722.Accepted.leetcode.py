class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        result = 0
        for val in A:
            if val % 2 == 0:
                result += val
        f_result = []
        for val_index in queries:
            val, index = val_index[0], val_index[1]
            prev_val = A[index]
            if prev_val % 2 == 0:
                result -= prev_val
            new_val = prev_val + val
            if new_val % 2 == 0:
                result += new_val
            A[index] = new_val
            f_result.append(result)
        return f_result
