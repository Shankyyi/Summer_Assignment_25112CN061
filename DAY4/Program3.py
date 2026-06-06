number = int(input("Enter a number to check: "))

temp = number
digits = len(str(number))
sum_of_powers = 0

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** digits
    temp //= 10

if number == sum_of_powers:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")