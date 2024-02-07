import sys
import u2py

def prtGreeting(name):
    print("Hello, ", name)
    inputStr = input()
    subrObj = u2py.Subroutine("PRINT.HELLO",0)
    subrObj.call()
    
def main():
    prtGreeting("Kish")

if __name__ == "__main__":
    main()
