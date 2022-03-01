#https://leetcode.com/problems/employee-importance/



"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def add_importance(self, emp_id):
        if emp_id not in self.importance_added:
            self.employee_cummulative_importance += self.dic[emp_id].importance
            self.importance_added.add(emp_id)
            if self.dic[emp_id].subordinates:
                for i in self.dic[emp_id].subordinates:
                    self.add_importance(i)
            
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.dic = {}
        for employee in employees:
            self.dic[employee.id] = employee
        self.importance_added = set()
        self.employee_cummulative_importance = 0
        self.add_importance(id)
        return self.employee_cummulative_importance
        
