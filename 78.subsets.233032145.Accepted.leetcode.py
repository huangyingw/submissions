class Solution(object):
    def subsets(self, nums):
        nums.sort()
        res = [[]]
        for index in range(len(nums)):
            size = len(res)
            for j in range(size):
                curr = list(res[j])
                curr.append(nums[index])
                res.append(curr)
        return res
if __name__ == "__main__":
    s = Solution()
