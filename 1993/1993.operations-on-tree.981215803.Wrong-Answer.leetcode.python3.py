from collections import defaultdict


class LockingTree:
    def __init__(self, parent):
        self.n = len(parent)
        self.parent = parent
        self.locked = [0] * self.n
        self.children = defaultdict(list)
        for child in range(1, self.n):
            self.children[parent[child]].append(child)

    def lock(self, num, user):
        if self.locked[num] == 0:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num, user):
        if self.locked[num] == user:
            self.locked[num] = 0
            return True
        return False

    def upgrade(self, num, user):

        if self.locked[num] != 0:
            return False

        node = self.parent[num]
        while node != -1:
            if self.locked[node] != 0:
                return False
            node = self.parent[node]

        locked_descendants = []
        stack = [num]
        while stack:
            node = stack.pop()
            if self.locked[node] != 0:
                locked_descendants.append(node)
            stack += self.children[node]
        if not locked_descendants:
            return False

        for desc in locked_descendants:
            if self.locked[desc] != user:
                return False

        for desc in locked_descendants:
            self.locked[desc] = 0
        self.locked[num] = user
        return True
