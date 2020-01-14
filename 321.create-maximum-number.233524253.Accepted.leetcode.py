class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        max_number = 0
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                max1 = self.max_single(nums1, i)
                max2 = self.max_single(nums2, k - i)
                merged = self.merge(max1, max2)
                max_number = max(max_number, int("".join(map(str, merged))))
        return [int(c) for c in str(max_number)]
    def max_single(self, nums, k):
        stack, n = [], len(nums)
        for i, num in enumerate(nums):
            while stack and num > stack[-1] and (len(stack) + (n - i) > k):
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack
    def merge(self, nums1, nums2):
        i, j = 0, 0
        merged = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                use1 = False
            elif nums1[i] > nums2[j]:
                use1 = True
            else:
                shift = 1
                while i + shift < len(nums1) and j + shift < len(nums2) and nums1[i + shift] == nums2[j + shift]:
                    shift += 1
                if i + shift == len(nums1):
                    use1 = False
                elif j + shift == len(nums2):
                    use1 = True
                elif nums2[j + shift] > nums1[i + shift]:
                    use1 = False
                else:
                    use1 = True
            if use1:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        return merged + nums1[i:] + nums2[j:]
