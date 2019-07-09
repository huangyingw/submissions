_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def canonical(s):
            evens = sorted([s[i] for i in range(0, len(s), 2)])
            odds = sorted([s[i] for i in range(1, len(s), 2)])
            return "".join(evens + odds)
        return len({canonical(s) for s in A})
