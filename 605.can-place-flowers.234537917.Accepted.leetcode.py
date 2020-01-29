class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        sum_0s = 0
        sum_flowers = 0
        flowerbed.append(1)
        for i in flowerbed:
            if i == 1:
                if sum_0s == 0:
                    continue
                else:
                    sum_flowers += (sum_0s - 1) / 2
                    sum_0s = 0
            else:
                sum_0s += 1
        return n <= sum_flowers

    def canPlaceFlowers(self, flowerbed, n):
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        count = 0
        for f in flowerbed:
            if f == 0:
                count += 1
            else:
                count = 0
            if count == 3:
                n -= 1
                count = 1
            if n == 0:
                return True
        return False
