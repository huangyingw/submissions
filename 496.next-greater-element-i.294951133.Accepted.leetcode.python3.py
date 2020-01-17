class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        result = [-1] * len(nums1)
        find_to_i = {}
        for i, num in enumerate(nums1):
            find_to_i[num] = i
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                if smaller in find_to_i:
                    result[find_to_i[smaller]] = num
            stack.append(num)
        return result
