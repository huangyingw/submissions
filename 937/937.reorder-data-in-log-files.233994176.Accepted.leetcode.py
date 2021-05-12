class Solution:
    def reorderLogFiles(self, logs):
        letters, numbers = [], []
        digits = {str(i) for i in range(10)}
        for log in logs:
            space = log.find(" ")
            first = log[space + 1]
            if first in digits:
                numbers.append(log)
            else:
                letters.append((log[space + 1:] + log[:space], log))
        letters.sort()
        return [log for _, log in letters] + numbers
