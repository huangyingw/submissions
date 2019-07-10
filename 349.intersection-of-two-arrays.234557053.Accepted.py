


class Solution(object):
    def intersection(self, nums1, nums2):

        d1, d2 = {}, {}
        for n in nums1:
            d1[n] = 0
        for n in nums2:
            if n in d1:
                d2[n] = 0
        return d2.keys()
