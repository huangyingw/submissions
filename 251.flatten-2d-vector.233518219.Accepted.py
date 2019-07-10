







class Vector2D(object):
    def __init__(self, vec2d):

        self.vec2d = vec2d
        self.list_nb, self.item_nb = 0, 0

        while self.list_nb < len(self.vec2d) and len(self.vec2d[self.list_nb]) == 0:
            self.list_nb += 1

    def next(self):

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

        return self.list_nb < len(self.vec2d)
