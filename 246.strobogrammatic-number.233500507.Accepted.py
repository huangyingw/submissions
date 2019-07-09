_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        strob = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        for left in range((len(num) + 1) // 2):
            right = len(num) - 1 - left
            if num[left] not in strob or strob[num[left]] != num[right]:
                return False
        return True
