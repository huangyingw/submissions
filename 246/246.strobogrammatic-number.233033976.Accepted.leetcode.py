class Solution(object):
    def isStrobogrammatic(self, num):
        dic = {'0': '0', '6': '9', '9': '6', '1': '1', '8': '8'}
        temp_s = ''
        for c in num[::-1]:
            if c not in dic:
                return False
            temp_s += dic[c]
        if int(temp_s) == int(num):
            return True
        return False
