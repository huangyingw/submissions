class Solution:
    def intersect(self, nums1, nums2):
        res = []
        nums1.sort()
        nums2.sort()
        pt1 = pt2 = 0
        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break
        return res
