class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):

            self.intersect(nums2, nums1)
        d = {}
        res = []
        for no in nums1:
            d[no] = d.get(no, 0) + 1
        for no in nums2:
            if no in d and d[no]:
                res.append(no)
                d[no] -= 1
        return res


class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
            self.intersect(nums2, nums1)
        nums1.sort()
        nums2.sort()
        p1 = p2 = 0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res
"""
What if elements of nums2 are stored on disk, and the memory is
limited such that you cannot load all elements into the memory at
once?
If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, 
read chunks of array that fit into the memory, and record the intersections.
If both nums1 and nums2 are so huge that neither fit into the memory, 
sort them individually (external sort), then read 2 elements from each 
array at a time in memory, record intersections.
"""
