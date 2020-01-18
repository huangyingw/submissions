class Solution(object):
    def dayOfYear(self, date):
        cumulative_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        year, month, day = [int(x) for x in date.split("-")]
        result = cumulative_days[month - 1] + day
        if month >= 3 and year % 4 == 0 and year != 1900:
            result += 1
        return result
