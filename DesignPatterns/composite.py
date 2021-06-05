# collection of multiple objects of similar type
import abc
from abc import ABC
from typing import List


class Employee(ABC):
    def __init__(self, _id, name, _type):
        self.name = name
        self._id = _id
        self._type = _type

    @abc.abstractmethod
    def show_employee_details(self) -> str: pass

    def __str__(self):
        return f"name:{self.name} id:{self._id} designation:{self._type}"


class Manager(Employee):

    def __init__(self, _id, name, _type="Manager"):
        super().__init__(_id, name, _type)

    def show_employee_details(self) -> str:
        pass

    def __str__(self):
        return super().__str__()


class IC(Employee):
    def show_employee_details(self) -> str:
        pass

    def __init__(self, _id, name, _type="IC"):
        super().__init__(_id, name, _type)

    def __str__(self):
        return super().__str__()


class EmployeeComposite:

    def __init__(self):
        self.employees: List[Employee] = []

    def add_employees(self, _employee: Employee):
        self.employees.append(_employee)
        return self

    def __iter__(self):
        for _employee in self.employees:
            yield _employee


if __name__ == "__main__":
    emp1 = Manager(32, "arnab")
    emp2 = Manager(33, "puchu")
    emp3 = IC(36, "polo")

    for employee in EmployeeComposite().add_employees(emp1).add_employees(emp2).add_employees(emp3):
        print(employee)
