class Solution(object):
    def canThreePartsEqualSum(self, A):
        total_sum = 0
        for val in A:
            total_sum += val
        if(total_sum % 3 != 0):
            return False
        curr_sum, groups = 0, 0
        for val in A:
            curr_sum += val
            if curr_sum == total_sum / 3:
                curr_sum = 0
                groups += 1
        return groups == 3
