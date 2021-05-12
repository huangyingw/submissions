class Solution(object):
    def maxSumDivThree(self, nums):
        total = sum(nums)
        rem = total % 3
        if rem == 0:
            return total
        rem_1 = [num for num in nums if num % 3 == 1]
        rem_2 = [num for num in nums if num % 3 == 2]
        rem_1.sort()
        rem_2.sort()
        candidates = [0]
        if rem == 1:
            if rem_1:
                candidates.append(total - rem_1[0])
            if len(rem_2) >= 2:
                candidates.append(total - sum(rem_2[:2]))
        elif rem == 2:
            if rem_2:
                candidates.append(total - rem_2[0])
            if len(rem_1) >= 2:
                candidates.append(total - sum(rem_1[:2]))
        return max(candidates)
