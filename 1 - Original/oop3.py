#
# Inherits, extends & Overrides
#
class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")
        return


class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level) -> None:
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f"{self.name} is debugging")

    def work(self):
        print(f"{self.name} is coding")
        return


class Designer(Employee):
    def draw(self):
        print(f"{self.name} is drawing")

    def work(self):
        print(f"{self.name} is designing")
        return


se = SoftwareEngineer("John", 30, 5000, "Junior")
print(se.name, se.age)
print(se.level)
se.work()
se.debug()

d = Designer("Paul", 25, 7000)
print(d.name, d.age)
d.work()
d.draw()


# Polymorphism

employees = [
    SoftwareEngineer("John", 30, 5000, "Junior"),
    SoftwareEngineer("Lisa", 55, 8000, "Manager"),
    Designer("Paul", 25, 7000),
]


def motivate_employees(employees):
    for employee in employees:
        print(employee.name, employee.age, employee.salary)
        employee.work()


motivate_employees(employees)
