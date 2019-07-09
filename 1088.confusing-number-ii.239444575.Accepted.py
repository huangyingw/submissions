class Solution(object):
    result = 0

    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        original_a = [0, 1, 6, 8, 9]
        o_rotation = [0, 1, 9, 8, 6]

        def recursive(original, rotation, digit, N):
            if original > N:
                return
            if original and original != rotation:
                self.result += 1
            start = original == 0
            if digit >= 1000000000:
                return
            for index in range(start, 5):
                recursive(original * 10 + original_a[index], rotation + o_rotation[index] * digit, digit * 10, N)
        recursive(0, 0, 1, N)
        if (N == 1000000000):
            self.result += 1
        return self.result
