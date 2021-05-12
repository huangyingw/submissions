class Solution(object):
    def countArrangement(self, N):
        used = [False for _ in range(N + 1)]
        self.count = 0

        def helper(i):
            if i == 0:
                self.count += 1
                return
            for num in range(1, N + 1):
                if not used[num] and (num % i == 0 or i % num == 0):
                    used[num] = True
                    helper(i - 1)
                    used[num] = False
        helper(N)
        return self.count
