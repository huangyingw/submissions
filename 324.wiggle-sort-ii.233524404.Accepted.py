









class Solution(object):
    def wiggleSort(self, nums):

        nums.sort()
        median = nums[len(nums) // 2]


        def mapping(i):
            return (i * 2 + 1) % (len(nums) | 1)


        left, i, right = 0, 0, len(nums) - 1
        while i <= right:
            if nums[mapping(i)] > median:
                nums[mapping(i)], nums[mapping(left)] = nums[mapping(left)], nums[mapping(i)]
                left += 1
                i += 1
            elif nums[mapping(i)] < median:
                nums[mapping(i)], nums[mapping(right)] = nums[mapping(right)], nums[mapping(i)]
                right -= 1
            else:
                i += 1
