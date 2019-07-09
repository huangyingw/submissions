_author_ = 'jake'
_project_ = 'leetcode'













class StringIterator(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.letter = None
        self.count = 0
        self.i = 0
        self.s = compressedString

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return " "
        if self.count == 0:
            self.move()
        self.count -= 1
        return self.letter

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count > 0 or self.i < len(self.s)

    def move(self):
        self.letter = self.s[self.i]
        self.count = 0
        self.i += 1
        while self.i < len(self.s) and self.s[self.i] <= "9":
            self.count = self.count * 10 + int(self.s[self.i])
            self.i += 1
