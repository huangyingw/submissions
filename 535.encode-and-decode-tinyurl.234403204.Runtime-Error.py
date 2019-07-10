class Solution:
    def dailyTemperatures1(self, T):
        nxt = [float('inf')] * 102
        ans = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            warmer_index = min(nxt[t] for t in range(T[i] + 1, 102))
            if warmer_index < float('inf'):
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans

    def dailyTemperatures2(self, T):
        ret = [0] * len(T)
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ret[i] = stack[-1] - i
            stack.append(i)
        return ret
