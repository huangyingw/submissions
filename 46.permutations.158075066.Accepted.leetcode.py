class Solution(object):
    def permute(self, nums):
        def helper():
            for index in range(len(nums)):
                if len(current) == len(nums):
                    result.append(list(current))
                    return

                if nums[index] not in current:
                    current.append(nums[index])
                    helper()
                    current.pop()

        current = []
        result = []
        helper()
        return result
