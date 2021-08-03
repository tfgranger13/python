# review OOP at the end of the course

# defining classes (blueprint for an object)
# taking data and assosciating behavior with it


# everything in python is an object
# dictionary is used because object means something specific

employee1 = {'first_name': 'Alex', 'last_name': 'Lasname', 'salary': 78000}
employee2 = {'first_name': 'Bob', 'last_name': 'Lasname-Jones', 'salary': 48000}
employee3 = {'first_name': 'Chaz', 'last_name': 'Smith', 'salary': 68000}
employee4 = {'first_name': 'Dale', 'last_name': 'Jones', 'salary': 98000}

employees = [employee1, employee2, employee3, employee4]

# for employee in employees:
#     print(f"{employee['first_name']} {employee['last_name']}")

employee4['last_name'] = 'Jones-Adams'

# for employee in employees:
#     print(f"{employee['first_name']} {employee['last_name']}")

employee5 = {'first_name': 'Harriet', 'last_name': 'Thespy', 'salary': 8000}

employees.append(employee5)


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



# create a class

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

    # string representation of object, change to contain data
    # default is the goblledygook because python doesn't know how to change the object into human understandable language
    # can add more to give more detail about these objects
    def __str__(self):
        return self.full_name

    
    def increase_salary_by_percentage(self, percentage):
        if (isinstance(percentage, float)):
            if (percentage>=0.8) and (percentage<=1.1):
                # can't change percentage by more than 1.1 or less than 0.8
                self.salary = self.salary * percentage


# create the employee
employee1 = Employee('Adam', 'Jones', 87000)

# same class, different attributes
employee2 = Employee('Carol', 'Schmidt', 99000)

# both humans, but distrinct from each other

print(employee1.first_name)


# combine data with behavior

employees = []
employees.append(Employee('Adam', 'Jones', 87000))
employees.append(Employee('Carol', 'Schmidt', 99000))
employees.append(Employee('Bob', 'Dole', 7000, middle_name = 'Abram'))

for employee in employees:
    # print(f"{employee.first_name} {employee.last_name}")
    print(f"{employee.full_name()}")
    # better done with encapsulation
    employee.salary = employee.salary * 1.02
    print(employee.salary)

# encapsulation
for employee in employees:
    employee.increase_salary_by_percentage(1.02)


    department_a = Department('Legal', '104c')

    emplyee_a = Employee('Adam', 'Jones', 87000, department_a)