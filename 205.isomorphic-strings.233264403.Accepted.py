_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_to_t = {}
        t_mapped = set()
        for cs, ct in zip(s, t):
            if cs in s_to_t:
                if s_to_t[cs] != ct:
                    return False
            elif ct in t_mapped:
                return False
            s_to_t[cs] = ct
            t_mapped.add(ct)
        return True
