def find_factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * find_factorial(num - 1)

number = int(input("Enter a number to find its factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = find_factorial(number)
    print(f"The factorial of {number} is {result}")