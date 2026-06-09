def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_of_digits(num // 10)

number = int(input("Enter a number: "))

actual_number = abs(number)

result = sum_of_digits(actual_number)
print(f"The sum of the digits of {number} is {result}")