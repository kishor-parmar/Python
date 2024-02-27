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

    # Instance Method
    def code(self):
        print(f"{self.name} is coding")

    def code_in_language(self, language):
        print(f"{self.name} coding in {language}")

    # Dunder Method
    def __str__(self) -> str:
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


# Instance
se1 = SoftwareEngineer("John", 35, "Junior", 5000)
se2 = SoftwareEngineer("Lisa", 55, "Senior", 8000)
se1.code()
se2.code()
print()

se1.code_in_language("Python")
se2.code_in_language("Java")
print()

print(se1)
print(se2)
print()

se3 = SoftwareEngineer("John", 35, "Junior", 5000)
print(se1 == se3)
print()

print(se1.entry_salary(20))
print(SoftwareEngineer.entry_salary(28))
