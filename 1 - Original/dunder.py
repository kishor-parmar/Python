class Human:
    def __init__(self, name, age, jobs=None):
        self.name = name
        self.age = age
        self.jobs = jobs

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Human(Name = {self.name}, Age = {self.age}"

    def __int__(self):
        return self.age

    def __hash__(self) -> int:
        return hash(self.name)

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.age + other.age

    def __iadd__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        self.age += other.age
        return self.age

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.age < other.age


print(Human("Kish", 64))
print(repr(Human("Kish", 64)))
print(int(Human("Kish", 64)))
print(hash(Human("Kish", 64)))

kish = Human("Kish", 64)
jason = Human("Jason", 30)
print(kish + jason)

kish += jason
print(kish)

print(kish == jason)

print(kish != jason)

kish = Human("Kish", 64)
jason = Human("Jason", 30)
print(kish < jason)
