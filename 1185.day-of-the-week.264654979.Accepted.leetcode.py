class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        cumulative_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        days = 4 + day + cumulative_days[month - 1] + 365 * (year - 1971)
        leap_days = (year - 1969) // 4
        if year % 4 == 0 and month >= 3:
            leap_days += 1
        days += leap_days
        return weekdays[days % 7]
