num = int(input("Enter a number: "))

sum_digits = 0

while num > 0:
    digit = num % 10      # extract last digit
    sum_digits += digit   # add digit to sum
    num = num // 10       # remove last digit

print("Sum of digits is:", sum_digits)