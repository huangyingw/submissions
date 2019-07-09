


class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        result = []
        if not A:
            return []
        str_bin = ''
        for val in A:
            str_bin += str(val)
            if(int(str_bin, 2) % 5 == 0):
                result.append(True)
            else:
                result.append(False)
        return result
