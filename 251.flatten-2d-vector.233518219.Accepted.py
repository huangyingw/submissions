_author_ = 'jake'
_project_ = 'leetcode'








class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.list_nb, self.item_nb = 0, 0

        while self.list_nb < len(self.vec2d) and len(self.vec2d[self.list_nb]) == 0:
            self.list_nb += 1

    def next(self):
        """
        :rtype: int
        """
        result = self.vec2d[self.list_nb][self.item_nb]
        if self.item_nb < len(self.vec2d[self.list_nb]) - 1:
            self.item_nb += 1
        else:
            self.item_nb = 0
            self.list_nb += 1
            while self.list_nb < len(self.vec2d) and len(self.vec2d[self.list_nb]) == 0:
                self.list_nb += 1
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.list_nb < len(self.vec2d)
