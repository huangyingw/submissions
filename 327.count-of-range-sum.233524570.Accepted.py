_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def countRangeSum(self, nums, lower, upper):

        cumul = [0]
        for num in nums:
            cumul.append(num + cumul[-1])

        def mergesort(cumul, left, right):
            count = 0
            if right - left <= 1:
                return count
            mid = (left + right) // 2
            count += mergesort(cumul, left, mid) + mergesort(cumul, mid, right)
            i, j = mid, mid
            for prefix_sum in cumul[left:mid]:
                while i < right and cumul[i] - prefix_sum < lower:
                    i += 1
                while j < right and cumul[j] - prefix_sum <= upper:
                    j += 1
                count += (j - i)
            cumul[left:right] = sorted(cumul[left:right])
            return count
        return mergesort(cumul, 0, len(cumul))
