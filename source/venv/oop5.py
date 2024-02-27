class SoftwareEngineer:
    def __init__(self) -> None:
        self._salary = None

    # Getter
    @property
    def salary(self):
        return self._salary

    # Setter
    @salary.setter
    def salary(self, value):
        self._salary = value

    # Deleter
    @salary.deleter
    def salary(self, value):
        del self._salary


se = SoftwareEngineer()

se.salary = 6000
print(se.salary)

del se.salary
print(se.salary)
