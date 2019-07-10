










class Solution(object):
    def maximumSwap(self, num):

        s = [int(c) for c in str(num)]
        max_seen, max_seen_i = -1, -1
        demote, promote = -1, -1
        for i in range(len(s) - 1, -1, -1):
            digit = s[i]
            if max_seen > digit:
                demote, promote = i, max_seen_i
            elif digit > max_seen:
                max_seen, max_seen_i = digit, i
        if demote == -1:
            return num
        s[demote], s[promote] = s[promote], s[demote]
        result = 0
        for digit in s:
            result = result * 10 + digit
        return result
