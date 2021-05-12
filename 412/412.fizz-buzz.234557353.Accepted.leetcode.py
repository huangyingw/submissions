class Solution:
    def fizzBuzz(self, n):
        result = []
        r5 = "Buzz"
        r3 = "Fizz"
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append(r3 + r5)
            elif i % 3 == 0:
                result.append(r3)
            elif i % 5 == 0:
                result.append(r5)
            else:
                result.append(str(i))
        return result
