from collections import defaultdict


class Solution(object):
    def minimumSemesters(self, N, relations):
        course_to_next = defaultdict(list)
        prerequisite_count = defaultdict(int)
        for pre, post in relations:
            course_to_next[pre].append(post)
            prerequisite_count[post] += 1
        no_preresquisites = [course for course in range(1, N + 1) if prerequisite_count[course] == 0]
        taken, semesters = 0, 0
        while no_preresquisites:
            new_no_preresquisites = []
            for course in no_preresquisites:
                for next_course in course_to_next[course]:
                    prerequisite_count[next_course] -= 1
                    if prerequisite_count[next_course] == 0:
                        new_no_preresquisites.append(next_course)
            semesters += 1
            taken += len(no_preresquisites)
            if taken == N:
                return semesters
            no_preresquisites = new_no_preresquisites
        return -1
