_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    def search(self, reader, target):

        left, right = 0, 20000
        while left <= right:
            mid = (left + right) // 2
            val = reader.get(mid)
            if target == val:
                return mid
            if target > val:
                left = mid + 1
            else:
                right = mid - 1
        return -1
