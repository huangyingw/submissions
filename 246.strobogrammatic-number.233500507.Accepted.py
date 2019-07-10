








class Solution(object):
    def isStrobogrammatic(self, num):

        strob = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        for left in range((len(num) + 1) // 2):
            right = len(num) - 1 - left
            if num[left] not in strob or strob[num[left]] != num[right]:
                return False
        return True
