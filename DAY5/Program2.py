number = int(input("Enter a number to check: "))

temp = number
sum_of_factorials = 0

while temp > 0:
    digit = temp % 10
    
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
        
    sum_of_factorials += factorial
    temp //= 10

if sum_of_factorials == number:
    print(f"{number} is a Strong number.")
else:
    print(f"{number} is not a Strong number.")