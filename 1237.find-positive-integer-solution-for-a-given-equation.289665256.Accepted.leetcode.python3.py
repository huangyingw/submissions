class Solution(object):
    def findSolution(self, customfunction, z):
        result = []
        for i in range(1, 101):
            for j in range(1, 101):
                temp = customfunction.f(i, j)
                if temp == z:
                    result.append([i, j])
                elif temp > z:
                    break
        return result
