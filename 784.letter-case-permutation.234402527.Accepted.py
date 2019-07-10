class Solution:
    def letterCasePermutation(self, S):
        import itertools
        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*L)]
