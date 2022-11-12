def divide():
    c = a / b
    return c

def multiply():
    c = a * b
    return c

def add():
    c = a + b
    return c

def subtract():
    c = a - b
    return c

print("Welcome to the 2 Digit Operations Python Calculator")
a = int(input("What is your first number?"))
b = int(input("What is your second number"))
print("/ = Divison, * = Multiplication, + = Addition, - = Subtraction")
print("Choose an Operation")
choose_operation = input()

if choose_operation == "/":
    print(divide())
elif choose_operation == "*":
    print(multiply())
elif choose_operation == "+":
    print(add())
elif choose_operation == "-":
    print(subtract())
else:
    print("Choose an Operation")