class Solution(object):
    def strobogrammaticInRange(self, low, high):
        if int(low) >= int(high):
            return 1 if low == high else 0
        if len(low) == len(high):
            arr = self.findStrobogrammatic(len(low))
            return len(list(filter(lambda c: low <= c <= high, arr)))
        else:
            res = 0
            for i in range(len(low), len(high) + 1):
                arr = self.findStrobogrammatic(i)
                if i == len(low):
                    res += len(list(filter(lambda c: low <= c, arr)))
                elif i == len(high):
                    res += len(list(filter(lambda c: c <= high, arr)))
                else:
                    res += len(arr)
            return res

    def findStrobogrammatic(self, n):
        def dfs(arr, length, curLen, curString, isOdd):
            elements = ['0', '1', '6', '8', '9']
            if curLen == length:
                d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
                if isOdd:
                    for i in curString[:-1][::-1]:
                        curString += d[i]
                else:
                    for i in curString[::-1]:
                        curString += d[i]
                arr.append(curString)
                return
            if curLen < length:
                if curLen == length - 1 and isOdd:
                    for i in ['0', '1', '8']:
                        dfs(arr, length, curLen + 1, curString + i, isOdd)
                elif curLen == 0:
                    for i in elements[1:]:
                        dfs(arr, length, curLen + 1, curString + i, isOdd)
                else:
                    for i in elements:
                        dfs(arr, length, curLen + 1, curString + i, isOdd)
        arr = []
        if n % 2 == 0:
            dfs(arr, n // 2, 0, "", False)
        else:
            dfs(arr, (n + 1) // 2, 0, "", True)
        return arr
