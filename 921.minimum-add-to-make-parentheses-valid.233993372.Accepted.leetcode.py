class Solution:
    def minAddToMakeValid(self, S):
        additions = 0
        net_open = 0
        for c in S:
            net_open += 1 if c == "(" else -1
            if net_open == -1:
                additions += 1
                net_open = 0
        return additions + net_open
