















class Solution(object):
    def numDecodings(self, s):

        ways = 0
        if s[0] == "*":
            ways = 9
        elif s[0] != "0":
            ways = 1
        prev_char = s[0]
        prev_ways = 1
        for c in s[1:]:
            new = 0

            if c == "*":
                new = 9 * ways
            elif c != "0":
                new = ways

            if prev_char == "*":
                if c == "*":
                    new += prev_ways * 15
                elif "0" <= c <= "6":
                    new += prev_ways * 2
                elif "7" <= c <= "9":
                    new += prev_ways
            elif prev_char == "1":
                if c == "*":
                    new += prev_ways * 9
                else:
                    new += prev_ways
            elif prev_char == "2":
                if c == "*":
                    new += prev_ways * 6
                elif c <= "6":
                    new += prev_ways
            new %= 10 ** 9 + 7
            prev_ways, ways = ways, new
            prev_char = c
        return ways
