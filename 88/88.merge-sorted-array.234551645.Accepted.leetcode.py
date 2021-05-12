class Solution(object):
    def merge(self, nums1, m, nums2, n):
        m -= 1
        n -= 1
        l = m + n + 1
        while m >= 0 and n >= 0:
            if nums1[m] < nums2[n]:
                nums1[l] = nums2[n]
                n -= 1
            else:
                nums1[l] = nums1[m]
                m -= 1
            l -= 1
        while n >= 0:
            nums1[l] = nums2[n]
            n -= 1
            l -= 1
