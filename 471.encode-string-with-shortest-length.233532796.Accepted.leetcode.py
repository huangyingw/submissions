class Solution(object):
    def encode(self, s, memo={}):
        if s in memo:
            return memo[s]
        encodings = [s]
        i = (s + s).find(s, 1)
        if i != -1 and i != len(s):
            encodings.append(str(len(s) // i) + "[" + self.encode(s[:i], memo) + "]")
        for i in range(1, len(s)):
            encodings.append(self.encode(s[:i], memo) + self.encode(s[i:], memo))
        result = min(encodings, key=len)
        memo[s] = result
        return result
