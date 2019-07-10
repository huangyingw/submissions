













class Solution(object):
    def findContestMatch(self, n):

        result = [str(i) for i in range(1, n + 1)]
        while len(result) > 1:
            new_result = []
            for i in range(len(result) // 2):
                new_result.append("(" + result[i] + "," + result[len(result) - i - 1] + ")")
            result = new_result
        return result[0]
