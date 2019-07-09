_author_ = 'jake'
_project_ = 'leetcode'















class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        importance, subordinates = {}, {}
        for employee in employees:
            importance[employee.id] = employee.importance
            subordinates[employee.id] = employee.subordinates

        def sum_importance(emp_id):
            total = importance[emp_id]
            for sub in subordinates[emp_id]:
                total += sum_importance(sub)
            return total
        return sum_importance(id)
