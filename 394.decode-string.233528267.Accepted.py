_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        repeats = 0
        digits = set("0123456789")
        for c in s:
            if c == "]":
                item = stack.pop()
                current = []
                while not isinstance(item, int):
                    current.append(item)
                    item = stack.pop()
                stack += (current[::-1] * item)
            elif c in digits:
                repeats = repeats * 10 + int(c)
            elif c == "[":
                stack.append(repeats)
                repeats = 0
            else:
                stack.append(c)
        return "".join(stack)


class Solution2(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.i = 0
        return "".join(self.decode(s))

    def decode(self, s):
        result = []
        while self.i < len(s) and s[self.i] != "]":
            if s[self.i] not in "0123456789":
                result.append(s[self.i])
                self.i += 1
            else:
                repeats = 0
                while s[self.i] in "0123456789":
                    repeats = repeats * 10 + int(s[self.i])
                    self.i += 1
                self.i += 1
                result += (self.decode(s) * repeats)
                self.i += 1
        return result
