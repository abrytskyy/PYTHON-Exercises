#1. Create a class Employee that stores the name, surname, and salary of an employee.
#
# Implement class methods to create employees from a string in the format "Name Surname Salary" and to display
# information about all employees.
#
# Implement a static method to calculate the average salary of employees.
#
# Implement an instance method to increase the salary of an employee by a specified percentage.

class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    @classmethod
    def create_employees_from_string(cls, Name, Surname, Salary):
        pass

    @staticmethod

