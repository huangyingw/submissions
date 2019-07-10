_project_ = 'leetcode'











class Solution(object):
    def canThreePartsEqualSum(self, A):

        partition, remainder = divmod(sum(A), 3)
        if remainder != 0:
            return False
        subarray = 0
        partitions = 0
        for num in A:
            subarray += num
            if subarray == partition:
                partitions += 1
                subarray = 0
        return partitions >= 3
