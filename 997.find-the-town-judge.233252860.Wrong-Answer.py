class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust:
            return 1
        mapping = {}
        unique = set()
        for truste_list in trust:
            unique.add(truste_list[0])
            if truste_list[1] in mapping:
                mapping[truste_list[1]] += 1
            else:
                mapping[truste_list[1]] = 1
        unique_set = len(unique)
        for key, value in mapping.items():
            if value == unique_set:
                return key
        return -1
