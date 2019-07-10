


class Solution(object):
    def majorityElement(self, nums):
        c, ans = 0, 0
        for i in nums:
            if c == 0:
                c += 1
                ans = i
            elif ans == i:
                c += 1
            else:
                c -= 1
        return ans
