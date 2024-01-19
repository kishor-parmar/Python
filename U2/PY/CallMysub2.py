import u2py

sub = u2py.Subroutine("MYSUB", 2)
sub.args[0]="Kish2"
sub.call()

result = sub.args

print(result)
print(len(result))
for value in result:
    print(value)