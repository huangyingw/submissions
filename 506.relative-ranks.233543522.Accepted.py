








class Solution(object):
    def findRelativeRanks(self, nums):

        num_i = [(num, i) for i, num in enumerate(nums)]
        num_i.sort(reverse=True)
        result = [None for _ in range(len(nums))]
        medals = ["Gold", "Silver", "Bronze"]
        for rank, (_, i) in enumerate(num_i):
            if rank < 3:
                result[i] = medals[rank] + " Medal"
            else:
                result[i] = str(rank + 1)
        return result
