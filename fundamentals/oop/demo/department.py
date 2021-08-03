
from employee import Employee

class Department():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.employees = []

    def add_employee(self, employee, department):
        if isinstance(employee, Employee):
            employee.department = department
            self.employees.append(employee)

    def list_employees(self):
        output = ""
        for employee in self.employees:
            output += f"{employee.full_name} - {employee.salary}\n"

    def remove_employee(self, employee_index):
        if employee_index>=0 and employee_index < len(self.employees):
            self.employees.pop(employee_index)
            return employee

    def transfer_employee(self, other_department, employee_index):
        if employee_index>=0 and employee_index < len(self.employees):
            employee_to_transfer = self.remove_employee(employee_index)
            other_department.add