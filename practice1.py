import math

print("+ - * / sin cos tan SQRT: ")
op = input()

if op == "+":
    a = int(input("enter number 1: "))
    b = int(input("enter number 2: "))
    result = a+b
if op == "-":
    a = int(input("enter number 1: "))
    b = int(input("enter number 2: "))
    result = a-b
if op == "*":
    a = int(input("enter number 1: "))
    b = int(input("enter number 2: "))
    result = a*b
if op == "/":
    a = int(input("enter number 1: "))
    b = int(input("enter number 2: "))
    if b == 0:
        result = "!!"
    else:
        result = a/b
if op == "sin":
    a = int(input("enter number: "))
    result = math.sin(a)
if op == "cos":
    a = int(input("enter number: "))
    result = math.cos(a)
if op == "tan":
    a = int(input("enter number: "))
    result = math.tan(a)
if op == "SQRT" or "sqrt":
    a = int(input("enter number: "))
    result = math.sqrt(a)
else:
    print("Error!")
print(result)
