class Solution:
    def longestPalindrome(self, s):
        res = 0
        flag = 0
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for c in count.values():
            if c % 2 == 0:
                res += c
            else:
                res += c - 1
                flag = 1
        if flag == 1:
            return res + 1
        return res
    def longestPalindrome(self, s):
        letter = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(j) for j in range(ord('A'), ord('Z') + 1)]
        result = 0
        for i in letter:
            result += s.count(i) // 2
        ind = 0
        for i in letter:
            if s.count(i) % 2 == 1:
                ind = 1
                break
        result = 2 * result + ind
        return result
