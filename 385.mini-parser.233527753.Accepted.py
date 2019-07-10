_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def deserialize(self, s):

        return self.helper(eval(s))

    def helper(self, s_eval):
        if isinstance(s_eval, int):
            return NestedInteger(s_eval)
        nested = NestedInteger()
        for item in s_eval:
            nested.add(self.helper(item))
        return nested
