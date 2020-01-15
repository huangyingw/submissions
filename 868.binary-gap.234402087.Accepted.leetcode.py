class Solution:
    def binaryGap(self, N):
        temp = bin(N)
        if temp.count('1') <= 1:
            return 0
        return len(max(bin(N)[2:].split('1')[1:-1], key=len)) + 1


class Solution:
    def binaryGap(self, N):
        max = 0
        str = bin(N)[2:]
        lst = []
        for i in range(len(str)):
            if int(str[i]) == 1:
                lst.append(i)
        if len(lst) < 2:
            return 0
        for i in range(len(lst)):
            if max < lst[i] - lst[i - 1]:
                max = lst[i] - lst[i - 1]
        return max


class Solution:
    def binaryGap(self, N):
        n = str(bin(N))
        count = 0
        last = n.index('1')
        for i in range(last + 1, len(n)):
            if n[i] == '1':
                if count < i - last:
                    count = i - last
                last = i
        return count
