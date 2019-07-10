




















class Solution(object):
    def leastOpsExpressTarget(self, x, target):

        pos = neg = powers = 0
        while target:
            target, remainder = divmod(target, x)
            if powers == 0:
                pos, neg = remainder * 2, (x - remainder) * 2
            else:
                pos, neg = min(remainder * powers + pos, (remainder + 1) * powers + neg), \
                    min((x - remainder) * powers + pos, (x - remainder - 1) * powers + neg)
            powers += 1
        return min(pos, powers + neg) - 1
