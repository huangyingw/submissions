_author_ = 'jake'
_project_ = 'leetcode'


















class Solution(object):
    def pushDominoes(self, dominos):

        prev_R = float("-inf")
        rights = []
        for i, c in enumerate(dominos):
            rights.append(prev_R)
            if c == "R":
                prev_R = i
            elif c == "L":
                prev_R = float("-inf")
        prev_L = float("inf")
        lefts = [0] * len(dominos)
        for i in range(len(dominos) - 1, -1, -1):
            lefts[i] = prev_L
            if dominos[i] == "L":
                prev_L = i
            elif dominos[i] == "R":
                prev_L = float("inf")
        dominos = [c for c in dominos]
        for i in range(len(dominos)):
            if dominos[i] == ".":
                diff = (lefts[i] - i) - (i - rights[i])
                if diff < 0:
                    dominos[i] = "L"
                elif diff > 0:
                    dominos[i] = "R"
        return "".join(dominos)
