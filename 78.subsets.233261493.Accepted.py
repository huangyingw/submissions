_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def subsets(self, nums):

        nb_subsets = 2**len(nums)
        all_subsets = []
        for subset_nb in range(nb_subsets):
            subset = []
            for num in nums:
                if subset_nb % 2 == 1:
                    subset.append(num)
                subset_nb //= 2
            all_subsets.append(subset)
        return all_subsets
