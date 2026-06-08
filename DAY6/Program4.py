x = float(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))

result = 1.0
exponent = n

if n < 0:
    exponent = -n

for i in range(exponent):
    result *= x

if n < 0:
    result = 1.0 / result

print(f"{x} raised to the power of {n} is {result}")