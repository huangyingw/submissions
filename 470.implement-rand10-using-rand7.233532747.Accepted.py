_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        units = rand7() - 1
        sevens = rand7() - 1
        num = 7 * sevens + units
        if num >= 40:
            return self.rand10()
        return (num % 10) + 1
