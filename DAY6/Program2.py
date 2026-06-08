binary_num = input("Enter a binary number: ")

decimal_val = 0
base = 1

for digit in reversed(binary_num):
    if digit == '1':
        decimal_val += base
    base *= 2

print(f"The decimal equivalent of {binary_num} is {decimal_val}")