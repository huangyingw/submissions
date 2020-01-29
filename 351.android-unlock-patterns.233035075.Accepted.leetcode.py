class Solution(object):
    def numberOfPatterns(self, m, n):
        used = [False] * 9
        res = 0
        for l in range(m, n + 1):
            res += self.calc_patterns(used, -1, l)
            used = [False] * 9
        return res

    def is_valid(self, used, index, last):
        if used[index]:
            return False
        if last == -1:
            return True
        if (last + index) % 2 == 1:
            return True
        mid = (last + index) // 2
        if mid == 4:
            return used[mid]
        if (index % 3 != last % 3) and (index // 3 != last // 3):
            return True
        return used[mid]

    def calc_patterns(self, used, last, length):
        if length == 0:
            return 1
        res = 0
        for i in range(9):
            if self.is_valid(used, i, last):
                used[i] = True
                res += self.calc_patterns(used, i, length - 1)
                used[i] = False
        return res
