def find_maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

result = find_maximum(number1, number2)

print("The maximum number is:", result)