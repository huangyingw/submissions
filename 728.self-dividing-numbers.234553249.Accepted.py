


class Solution:
    def selfDividingNumbers(self, left, right):
        numbers = []
        for i in range(left, right + 1):
            if i < 10:
                numbers.append(i)
            else:
                temp = i
                flag = 0
                while temp > 0:
                    n = temp % 10
                    if n == 0:
                        flag = 1
                        break
                    else:
                        if i % n != 0:
                            flag = 1
                            break
                    temp = temp // 10
                if flag == 0:
                    numbers.append(i)
        return numbers
