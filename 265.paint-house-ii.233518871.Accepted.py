_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def minCostII(self, costs):

        if not costs or not costs[0]:
            return 0
        for i in range(1, len(costs)):
            min_colours = [0, 1]
            if costs[i - 1][0] > costs[i - 1][1]:
                min_colours = [1, 0]
            for colour in range(2, len(costs[0])):
                if costs[i - 1][colour] <= costs[i - 1][min_colours[0]]:
                    min_colours[1], min_colours[0] = min_colours[0], colour
                elif costs[i - 1][colour] < costs[i - 1][min_colours[1]]:
                    min_colours[1] = colour
            for colour in range(len(costs[0])):
                costs[i][colour] += costs[i - 1][min_colours[colour == min_colours[0]]]
        return min(costs[-1])
