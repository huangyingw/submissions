"""

class Employee(object):
  def __init__(self, id, importance, subordinates):


    self.id = id

    self.importance = importance

    self.subordinates = subordinates
"""


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        totalImportanceValue = 0

        sub_ids = [id]
        idToEmployeesIndex = {}
        for i in range(len(employees)):
            idToEmployeesIndex[employees[i].id] = i
        while len(sub_ids) != 0:
            now_id = sub_ids.pop(0)
            totalImportanceValue += employees[idToEmployeesIndex[now_id]].importance
            sub_ids.extend(employees[idToEmployeesIndex[now_id]].subordinates)
        return totalImportanceValue
