from department import Department
from employee import Employee



class Employee():
    # classes have methods
    # use def just like defining a function
    # double underscores indicate overwriting a base part of an object's functionality
    # self is the first parameter included
    def __init__(self, first_name, last_name, salary, department, middle_name = None,):
        # these are properties or attributes
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.middle_name = middle_name
        self.department = department
        department.add_employee(self)

    def full_name(self):
        if self.middle_name == None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"