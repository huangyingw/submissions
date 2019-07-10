








from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):

        order = []
        nb_prerequisites = defaultdict(int)
        prereq_list = defaultdict(list)
        for after, before in prerequisites:
            nb_prerequisites[after] += 1
            prereq_list[before].append(after)
        can_take = set(i for i in range(numCourses)) - set(nb_prerequisites.keys())
        while can_take:
            course = can_take.pop()
            order.append(course)
            for dependent in prereq_list[course]:
                nb_prerequisites[dependent] -= 1
                if nb_prerequisites[dependent] == 0:
                    can_take.add(dependent)
        return order if len(order) == numCourses else []
