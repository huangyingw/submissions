class Solution(object):
    def probabilityOfHeads(self, prob, target):
        probs = [1]
        for coin in prob:
            new_probs = [0] * (len(probs) + 1)
            for heads, p in enumerate(probs[:target + 1]):
                new_probs[heads] += p * (1 - coin)
                new_probs[heads + 1] += p * coin
            probs = new_probs
        return probs[target]
