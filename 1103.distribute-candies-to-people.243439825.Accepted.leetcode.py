class Solution(object):
    def distributeCandies(self, candies, num_people):
        people_served = int(((1 + 8 * candies) ** 0.5 - 1) / 2)
        cycles = people_served / num_people
        result = [0] * num_people
        if cycles != 0:
            base = num_people * (cycles - 1) * cycles / 2
            for i in range(num_people):
                result[i] += base + cycles * (i + 1)
        last_candies = cycles * num_people
        candies -= sum(result)
        for i in range(num_people):
            if candies <= 0:
                break
            result[i] += min(candies, last_candies + i + 1)
            candies -= last_candies + i + 1
        return result
