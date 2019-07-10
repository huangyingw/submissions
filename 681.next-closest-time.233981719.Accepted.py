_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def nextClosestTime(self, time):

        result = [c for c in time]
        digits = set(int(c) for c in time[:2] + time[3:])
        min_digit = min(digits)
        max_digits = {0: 2, 3: 5, 4: 9}

        def increase(i):
            if i == 1:
                if time[0] == "2":
                    max_digit = 3
                else:
                    max_digit = 9
            else:
                max_digit = max_digits[i]
            larger_digits = [d for d in digits if int(time[i]) < d <= max_digit]
            return min(larger_digits) if larger_digits else -1
        for i in [4, 3, 1, 0]:
            increaseed = increase(i)
            if increaseed != -1:
                result[i] = str(increaseed)
                break
            else:
                result[i] = str(min_digit)
        return "".join(result)
