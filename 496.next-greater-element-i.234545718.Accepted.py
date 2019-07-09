
class Solution:




    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l2 = len(nums2)
        nums2_next = [-1] * l2
        for i in range(l2 - 1):
            for j in range(i + 1, l2):
                if nums2[j] > nums2[i]:
                    nums2_next[i] = nums2[j]
                    break
        res = []
        for k in nums1:
            res.append(nums2_next[nums2.index(k)])
        return res



    def nextGreaterElement2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        nextGreat = {}
        nums3 = []
        res = []
        for num in nums2:
            while nums3 and nums3[-1] < num:
                nextGreat[nums3[-1]] = num
                nums3.pop()
            nums3.append(num)
        for num in nums1:
            if num in nextGreat:
                res.append(nextGreat[num])
            else:
                res.append(-1)
        return res
