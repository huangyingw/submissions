











import heapq


class Solution(object):
    def scheduleCourse(self, courses):

        total_length = 0
        taken_courses = []
        courses.sort(key=lambda c: c[1])
        for duration, end in courses:
            if total_length + duration <= end:
                total_length += duration
                heapq.heappush(taken_courses, -duration)
            elif -taken_courses[0] > duration:
                neg_longest = heapq.heappushpop(taken_courses, -duration)
                total_length += neg_longest + duration
        return len(taken_courses)
