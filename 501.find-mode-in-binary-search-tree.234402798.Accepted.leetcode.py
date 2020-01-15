class Solution:
    def findMode(self, root):
        self.mode = set()
        self.max_freq = 0
        self.cur_freq = 0
        self.cur_item = None
        if root:
            self.inorder(root)
        return list(self.mode)

    def calc_freq(self, value):
        if self.cur_item == value:
            self.cur_freq += 1
        else:
            self.cur_item = value
            self.cur_freq = 1
        if self.max_freq < self.cur_freq:
            self.mode = set([self.cur_item])
            self.max_freq = self.cur_freq
        elif self.max_freq == self.cur_freq:
            self.mode.append(self.cur_item)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.calc_freq(root.val)
            self.inorder(root.right)


class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        pre, cur, stack, cur_count, max_count, modes = None, root, [], 0, 0, []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not pre or cur.val == pre.val:
                cur_count += 1
            else:
                if cur_count > max_count:
                    max_count = cur_count
                    modes = [pre.val]
                elif cur_count == max_count:
                    modes.append(pre.val)
                cur_count = 1
            pre = cur
            cur = cur.right
        if cur_count > max_count:
            return [pre.val]
        elif cur_count == max_count:
            modes.append(pre.val)
        return modes
