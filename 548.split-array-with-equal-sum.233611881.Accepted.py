












class Solution(object):
    def splitArray(self, nums):

        n = len(nums)
        if n < 7:
            return False
        cumul = [nums[0]]
        for num in nums[1:]:
            cumul.append(num + cumul[-1])
        for j in range(3, n - 3):
            candidates = set()
            for i in range(1, j - 1):
                left_sum = cumul[i - 1]
                right_sum = cumul[j - 1] - cumul[i]
                if left_sum == right_sum:
                    candidates.add(left_sum)
            for k in range(j + 2, n - 1):
                left_sum = cumul[k - 1] - cumul[j]
                right_sum = cumul[n - 1] - cumul[k]
                if left_sum == right_sum and left_sum in candidates:
                    return True
        return False
