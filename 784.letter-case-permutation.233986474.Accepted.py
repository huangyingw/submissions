_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def letterCasePermutation(self, S):

        permutations = [[]]
        for c in S:
            if "0" <= c <= "9":
                for perm in permutations:
                    perm.append(c)
            else:
                new_permutations = []
                upper, lower = c.upper(), c.lower()
                for perm in permutations:
                    new_permutations.append(perm + [upper])
                    perm.append(lower)
                    new_permutations.append(perm)
                permutations = new_permutations
        return ["".join(perm) for perm in permutations]
