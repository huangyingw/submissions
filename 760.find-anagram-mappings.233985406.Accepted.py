_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        B_to_int = {}
        for i, b in enumerate(B):
            B_to_int[b] = i
        result = []
        for a in A:
            result.append(B_to_int[a])
        return result
