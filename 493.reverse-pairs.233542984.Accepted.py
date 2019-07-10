







class Solution(object):
    def reversePairs(self, nums):

        self.pairs = 0

        def mergesort(nums):
            if len(nums) < 2:
                return nums
            mid = len(nums) // 2
            left = mergesort(nums[:mid])
            right = mergesort(nums[mid:])
            return merge(left, right)

        def merge(left, right):
            j = 0
            for num in left:
                while j < len(right) and num > 2 * right[j]:
                    j += 1
                self.pairs += j

            merged = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            return merged + left[i:] + right[j:]
        mergesort(nums)
        return self.pairs
