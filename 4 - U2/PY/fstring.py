from datetime import datetime

now: datetime = datetime.now()

print(f"{now:%d-%m-%y (%H:%M:%S)}")
print(f"{now:%c}")
print(f"{now:%I%p}")
print()

n: int = 1000000000
print(f"{n:_}")
print(f"{n:,}")
print()

x: float = 1234.5678
print(f"Result = {x:.2f}")
print(f"Result = {x:.0f}")
print(f"Result = {x:,.3f}")
print()


var: str = "var"
print(f"{var:_<20}:")
print(f"{var:#>20}:")
print(f"{var:|^20}:")
print()


a: int = 5
b: int = 10
my_var: str = "Hello World"
print(f"{a + b = }")
print(f"{my_var = }")
