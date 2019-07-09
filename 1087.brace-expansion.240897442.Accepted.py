_author_ = 'jake'
_project_ = 'leetcode'















class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        group_start = 0
        groups = []
        while group_start < len(S):
            while S[group_start] in "}{":
                group_start += 1
            group_end = group_start
            while group_end < len(S) and S[group_end] not in "{}":
                group_end += 1
            groups.append(sorted(S[group_start:group_end].split(",")))
            group_start = group_end + 1
        results = []

        def expand(group, partial):
            if group == len(groups):
                results.append(partial)
                return
            for c in groups[group]:
                expand(group + 1, partial + c)
        expand(0, "")
        return results
