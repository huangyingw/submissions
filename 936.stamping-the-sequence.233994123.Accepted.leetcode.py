class Solution:
    def movesToStamp(self, stamp, target):
        memo = {}
        def helper(i, j, results):
            if (i, j) in memo:
                return memo[(i, j)]
            if len(results) > 10 * len(target):
                return []
            if i == len(target):
                return results if j == len(stamp) else []
            if j == len(stamp):
                for k in range(len(stamp)):
                    temp = helper(i, k, [i - k] + results)
                    if temp:
                        result = temp
                        break
                else:
                    result = []
            elif target[i] != stamp[j]:
                result = []
            else:
                temp = helper(i + 1, j + 1, results)
                if temp:
                    result = temp
                else:
                    result = helper(i + 1, 0, results + [i + 1])
            memo[(i, j)] = result
            return result
        return helper(0, 0, [0])
