# Position, Name, Age, Salary


class SoftwareEngineer:

    # Class Attribute
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary) -> None:

        # Instance Attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


# Instance
se1 = SoftwareEngineer("John", 35, "Junior", 5000)
print(se1.name, se1.age)
print(se1.alias, SoftwareEngineer.alias)
