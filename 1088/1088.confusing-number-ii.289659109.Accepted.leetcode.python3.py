class Solution(object):
    def confusingNumberII(self, N):
        valid = [0, 1, 6, 8, 9]
        rotations = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        self.count = 0

        def helper(num, rotation):
            length = len(str(num))
            if num != rotation:
                self.count += 1
            for i in valid:
                if num * 10 + i > N:
                    return
                helper(num * 10 + i, rotations[i] * 10 ** length + rotation)
        for num in valid[1:]:
            helper(num, rotations[num])
        return self.count
