_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lexical = [1]
        while len(lexical) < n:
            num = lexical[-1] * 10
            while num > n:
                num //= 10
                num += 1
                while num % 10 == 0:
                    num //= 10
            lexical.append(num)
        return lexical


class Solution2(object):
    def lexicalOrder(self, n):
        strings = list(map(str, range(1, n + 1)))
        strings.sort()
        return list(map(int, strings))
