_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        min_right = [float("inf") for _ in range(len(arr))]
        for i in range(len(arr) - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], arr[i + 1])
        partitions = 0
        partition_max = None
        for i, num in enumerate(arr):
            partition_max = num if partition_max is None else max(partition_max, num)
            if partition_max < min_right[i]:
                partitions += 1
                partition_max = None
        return partitions
