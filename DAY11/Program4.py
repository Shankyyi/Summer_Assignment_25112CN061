def find_factorial(number):
    if number < 0:
        return "Factorial does not exist for negative numbers"
        
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial

num = int(input("Enter a number: "))
print("The factorial is:", find_factorial(num))