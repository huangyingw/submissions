class Solution(object):
    def compress(self, chars):
        n = len(chars)
        idx = 0
        cnt = 0
        for i in range(n):
            if chars[i] == chars[i - 1]:
                cnt += 1
            else:
                idx += 1
                if cnt > 1:
                    for j in str(cnt):
                        chars[idx] = j
                        idx += 1
                cnt = 0
        return idx
