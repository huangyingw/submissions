_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        self.num, self.target, self.expressions = num, target, []
        self.helper("", 0, 0, 0)
        return self.expressions

    def helper(self, path, index, eval, multed):
        if index == len(self.num) and self.target == eval:
            self.expressions.append(path)
        for i in range(index, len(self.num)):
            if i != index and self.num[index] == '0':
                break
            cur_str = self.num[index:i + 1]
            cur_int = int(cur_str)
            if index == 0:
                self.helper(path + cur_str, i + 1, cur_int, cur_int)
            else:
                self.helper(path + "+" + cur_str, i + 1, eval + cur_int, cur_int)
                self.helper(path + "-" + cur_str, i + 1, eval - cur_int, -cur_int)
                self.helper(path + "*" + cur_str, i + 1, eval - multed + multed * cur_int, multed * cur_int)
