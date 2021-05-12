class Solution(object):
    def permute(self, nums):
        permutations = [[]]
        for num in nums:
            new_permutations = []
            for perm in permutations:
                for i in range(0, len(perm) + 1):
                    new_permutations.append(perm[:i] + [num] + perm[i:])
            permutations = new_permutations
        return permutations


class Solution2(object):
    def permute(self, nums):
        return self.permute_helper(nums, 0)

    def permute_helper(self, nums, index):
        permutations = []
        if index >= len(nums):
            permutations.append(nums[:])
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            permutations += self.permute_helper(nums, index + 1)
            nums[i], nums[index] = nums[index], nums[i]
        return permutations
