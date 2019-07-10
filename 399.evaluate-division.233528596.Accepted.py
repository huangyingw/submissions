from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for i in range(len(equations)):
            num, den, val = equations[i][0], equations[i][1], values[i]
            graph[num][den] = val
            graph[den][num] = 1 / val
        for i in graph:
            for j in graph[i]:
                for k in graph[i]:
                    graph[j][k] = graph[j][i] * graph[i][k]
        results = []
        for num, den in queries:
            if num in graph and den in graph[num]:
                results.append(graph[num][den])
            else:
                results.append(-1)
        return results
