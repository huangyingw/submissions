
class Solution:

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(set(s)) != len(set(t)):
            return False
        alpha = set(s)
        for i in alpha:
            if s.count(i) != t.count(i):
                return False
        return True


    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        for i in s:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1
        for j in t:
            if j in dic2:
                dic2[j] += 1
            else:
                dic2[j] = 1
        return dic1 == dic2

    from collections import Counter

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_d = Counter(s)
        t_d = Counter(t)
        if len(s_d.keys()) != len(t_d.keys()):
            return False
        for key in s_d:
            if s_d[key] != t_d[key]:
                return False
        return True
