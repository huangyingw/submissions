class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        try:
            if isinstance(float(s), float) or isinstance(int(s), int):
                return True
        except Exception as e:
            return False
