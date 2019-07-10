

























class Solution(object):
    def maxVacationDays(self, flights, days):

        cities = len(flights)
        weeks = len(days[0])
        if not cities or not weeks:
            return 0
        prev_week_max_days = [0 for _ in range(cities)]
        for week in range(weeks - 1, -1, -1):
            this_week_max_days = [0 for _ in range(cities)]
            for start in range(cities):
                max_vacation = days[start][week] + prev_week_max_days[start]
                for end in range(cities):
                    if flights[start][end]:
                        max_vacation = max(max_vacation, days[end][week] + prev_week_max_days[end])
                this_week_max_days[start] = max_vacation
            prev_week_max_days = this_week_max_days
        return this_week_max_days[0]
