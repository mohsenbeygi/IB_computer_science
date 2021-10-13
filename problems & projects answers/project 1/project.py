a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
operator = input("Please enter the operator +, -, x, /, // or %: ")

if operator == "+":
    print(a + b)

elif operator == "-":
    print(a - b)

elif operator == "x":
    print(a * b)

elif operator == "/":
    print(a / b)

elif operator == "%":
    print(a % b)

elif operator == "//":
    print(a // b)

else:
    print("Error: not recognized operator")