class Solution(object):
    def getImportance(self, employees, id):
        DictE = {employee.id: employee for employee in employees}
        SelectL = [id]
        Total = 0
        while SelectL:
            select = SelectL.pop()
            Total += DictE[select].importance
            for sub in DictE[select].subordinates:
                SelectL.append(sub)
        return Total
