class Solution(object):
    def intersect(self, nums1, nums2):

        dic = {}
        for a in nums1:
            dic[a] = dic.get(a, 0) + 1
        res = []
        for a in nums2:
            if a in dic and dic[a] > 0:
                res.append(a)
                dic[a] -= 1
        return res
